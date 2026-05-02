import argparse
from datetime import datetime
import json
import os
import re
import sys


now = datetime.now()
date_added = now.strftime("%Y-%m-%d %H:%M")
json_path = "/tmp/tasks.json"


def task_options_prints():
    print("\n" + "="*32)
    print("        CLI TASK MANAGER")
    print("="*32)
    print("        [1] Add new task")
    print("        [2] Delete task")
    print("        [3] View all tasks")
    print("        [4] Complete task")
    print("        [5] Exit")
    print("="*32)


user_input= input("Please enter your task's title, task's priority, task's due date seperate them with ',': ")


def file_exist(path):
    return os.path.exists(path)


def take_task(user_task):
    user_task_split = re.split(r'\s*,\s*', user_task)
    user_task_keys = ["title", "priority", "due"]
    result = dict(zip(user_task_keys, user_task_split))
    result["date_added"] = date_added
    result["done"] = False
    return result


def add_task():
    if not file_exist(json_path):
        with open(json_path, 'w') as file:
            data = take_task(user_input)
            data["id"] = 1
            json.dump([data], file, indent=4, sort_keys=True)

    else:
        if os.path.getsize(json_path) > 0:
            with open(json_path, 'r') as file:
                data = json.load(file)
        else:
            data = []
            
        next_id = max((item['id'] for item in data), default=0) + 1

        new_entry = take_task(user_input)
        new_entry["id"] = next_id

        data.append(new_entry)
            
        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
    
    print("Your task been added.")


def delete_task(chosen_title):
    if file_exist(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            for i in range(len(data)-1, -1, -1):
                if data[i]["title"] == chosen_title:
                    data.pop(i)

        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)        
        return f"You're task {chosen_title} been successfully deleted."    
    return "There's no task here to delete."


def mark_down_task():
    pass


def interactive_mode():
    pass


def main():
    pass

task_options_prints()
add_task()
