# import datetime
import json
import os
import re

user_input= input("Please enter your task, task's priority, task's deadline seperate them with ',': ")

def take_task(user_task):
    user_task_split = re.split(r'\s*,\s*', user_task)
    user_task_keys = ["name", "priority", "deadline"]
    result = dict(zip(user_task_keys, user_task_split))
    return result

print(f"User's task information is {take_task(user_input)}.")

if not os.path.exists('/tmp/tasks.json'):
    with open('/tmp/tasks.json', 'w') as file:
        data = take_task(user_input)
        data["id"] = 1
        json.dump([data], file, indent=4, sort_keys=True)

else:
    with open('/tmp/tasks.json', 'r') as file:
        data = json.load(file)
        next_id = max((item['id'] for item in data), default=0) + 1

        new_entry = take_task(user_input)
        new_entry["id"] = next_id

        data.append(new_entry)
        
    with open('/tmp/tasks.json', 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

        