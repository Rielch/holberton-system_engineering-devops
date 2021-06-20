#!/usr/bin/python3
"""List all completed tasks for given user id"""
import requests
from sys import argv


if __name__ == "__main__":
    user_response = requests.get('https://jsonplaceholder.typicode.com/users\
                                ?id={}'.format(argv[1]))
    user = user_response.json()

    tasks_response = requests.get('https://jsonplaceholder.typicode.com/users/\
                                {}/todos'.format(argv[1]))
    tasks = tasks_response.json()

    total_tasks = 0
    completed_tasks = 0

    tasks_titles = []
    for task in tasks:
        total_tasks += 1
        if task["completed"] is True:
            completed_tasks += 1
            tasks_titles.append(task["title"])

    print("Employee {} is done with tasks {}/{}:".format(user[0]["name"],
                                                         completed_tasks,
                                                         total_tasks))
    for task in tasks_titles:
        print("\t {}".format(task))
