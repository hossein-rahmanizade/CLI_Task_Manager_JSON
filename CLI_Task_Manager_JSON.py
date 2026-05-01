import json
import datetime #TODO I'll add timestamp to user's input
import re

user_input= input("Please enter your task, task's priority, task's deadline seperate them with ',': ")

def take_task(user_task):
    user_task_split = re.split(r'\s*,\s*', user_task)
    user_task_keys = ["name", "priority", "deadline"]
    result = dict(zip(user_task_keys, user_task_split))
    return result

print(f"User's task information is {take_task(user_input)}.")

with open('/tmp/tasks.json', 'w') as file:
    data = take_task(user_input)
    json.dump(data, file)
