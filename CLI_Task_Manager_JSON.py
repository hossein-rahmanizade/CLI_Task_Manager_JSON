import json
import datetime

def take_task():
    user_task = input("Please enter your task, seperate them with ',': ")
    user_task_split = user_task.split(",")
    return user_task_split

user_list = take_task()
print(f"\nYou entered {len(user_list)} tasks.\n")

for index, item in enumerate(user_list, start=1):
    print(f"{index}-{item}")

