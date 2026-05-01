import argparse
from datetime import datetime
import json
import os
import re
import sys


user_input= input("Please enter your task, task's priority, task's deadline seperate them with ',': ")

now = datetime.now()
date_added = now.strftime("%Y-%m-%d %H:%M")

def take_task(user_task):
    user_task_split = re.split(r'\s*,\s*', user_task)
    user_task_keys = ["name", "priority", "deadline"]
    result = dict(zip(user_task_keys, user_task_split))
    result["date_added"] = date_added
    result["done"] = False
    return result


json_path = "/tmp/tasks.json"

def add_task():
    if not os.path.exists(json_path):
        with open(json_path, 'w') as file:
            data = take_task(user_input)
            data["id"] = 1
            json.dump([data], file, indent=4, sort_keys=True)

    else:
        with open(json_path, 'r') as file:
            data = json.load(file)
            next_id = max((item['id'] for item in data), default=0) + 1

            new_entry = take_task(user_input)
            new_entry["id"] = next_id

            data.append(new_entry)
            
        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
    
    print("Your task been added.")

add_task()


def delete_task(chosen_name):
    if os.path.exists(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            for i in range(len(data)-1, -1, -1):
                if data[i]["name"] == chosen_name:
                    data.pop(i)

        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)        
        return f"You're task {chosen_name} been deleted"    
    return "There's no task here to delete."


def mark_down_task():
    pass


def interactive_mode():
    pass

