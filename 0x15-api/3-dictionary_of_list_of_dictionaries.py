#!/usr/bin/python3
"""Exports all tasks from all users to a .json file"""
import json
import requests


if __name__ == "__main__":

    users_tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    users_dict = {}
    tasks_dict = {}

    for user in users:
        users_dict[user["id"]] = user["username"]
        tasks_dict[user["id"]] = []

    for task in users_tasks:
        task_dict = {}
        task_dict["username"] = users_dict[task["userId"]]
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        tasks_dict[task["userId"]].append(task_dict)

    with open('todo_all_employees.json', mode="w") as file:
        json.dump(tasks_dict, file)