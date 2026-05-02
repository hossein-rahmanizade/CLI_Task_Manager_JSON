import argparse
from datetime import datetime
import json
import os
import re
import sys


now = datetime.now()
date_added = now.strftime("%Y-%m-%d %H:%M")
json_path = "/tmp/tasks.json"


def task_options_prints(): # later I need to add edit task to it too.
    print("\n" + "="*32)
    print("        CLI TASK MANAGER")
    print("="*32)
    print("        [1] Add new task")
    print("        [2] Delete task")
    print("        [3] View all tasks")
    print("        [4] Complete task")
    print("        [5] Exit")
    print("="*32)


def file_exist(path):
    return os.path.exists(path)


def parse_task_input(user_task):
    user_task_split = re.split(r'\s*,\s*', user_task)
    user_task_keys = ["title", "priority", "due"]
    result = dict(zip(user_task_keys, user_task_split))
    result["date_added"] = date_added
    result["done"] = False
    return result


def add_task_to_file(task_input):
    if not file_exist(json_path):
        with open(json_path, 'w') as file:
            data = parse_task_input(task_input)
            data["id"] = 1
            json.dump([data], file, indent=4, sort_keys=True)

    else:
        if os.path.getsize(json_path) > 0:
            with open(json_path, 'r') as file:
                data = json.load(file)
        else:
            data = []
            
        next_id = max((item['id'] for item in data), default=0) + 1

        new_entry = parse_task_input(task_input)
        new_entry["id"] = next_id

        data.append(new_entry)
            
        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
    
    print("\nYour task been added.")


def delete_task(title):
    if file_exist(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            print()
            for i in range(len(data)-1, -1, -1):
                if data[i]["title"] == title:
                    data.pop(i)

        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)        
        print(f"You're task '{title}' been successfully deleted.")
        
    else:
        print("There's no task here to delete.")


def view_task(): # later I add parameters to filter the output like show_all=True
    if file_exist(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
        print()
        for i in range(len(data)):
            if not data[i]["done"]:
                print(f"[ ] {data[i]["id"]}. {data[i]["title"]} (due: {data[i]["due"]}) (priority: {data[i]["priority"]})")
            else:
                print(f"[x] {data[i]["id"]}. {data[i]["title"]} (due: {data[i]["due"]}) (priority: {data[i]["priority"]})")
    else:
        print("There's no task here to view.")


def mark_down_task():
    pass


def interactive_mode():
    pass


def main():

    while True:
        task_options_prints()
        choice = input("Choose option 1-5: ")

        if choice == "1":
            task_input = input("Enter title, priority, due: ")
            add_task_to_file(task_input)
        elif choice == "2":
            title = input("Enter task name to delete: ")
            delete_task(title)
        elif choice == "3":
            view_task()
        elif choice == "4":
            name = input("Enter task name to complete: ") # or id number
            mark_down_task(name)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("invalid choice")


main()