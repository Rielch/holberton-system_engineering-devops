#!/usr/bin/python3
"""Exports all tasks from a user to a .json file"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    user_tasks = requests.get('https://jsonplaceholder.\
typicode.com/users/{}/todos'.format(argv[1])).json()

    username = requests.get('https://jsonplaceholder.typicode.\
com/users?id={}'.format(argv[1])).json()[0]["username"]

    task_list = []
    for task in user_tasks:
        task_dict = {}
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        task_dict["username"] = username
        task_list.append(task_dict)

    user_dict = {argv[1]: task_list}

    with open('{}.json'.format(argv[1]), mode="w") as file:
        json.dump(user_dict, file)
