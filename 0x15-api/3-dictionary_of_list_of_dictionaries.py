#!/usr/bin/python3
"""
Script to export data from the API in JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users").json()

    all_tasks = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        tasks = requests.get(url + f"/todos?userId={user_id}").json()

        task_list = []
        for task in tasks:
            task_list.append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            })

        all_tasks[user_id] = task_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
