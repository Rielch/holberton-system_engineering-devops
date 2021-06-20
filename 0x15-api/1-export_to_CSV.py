#!/usr/bin/python3
"""Exports all tasks from a user to a .csv file"""
import requests
from sys import argv


if __name__ == "__main__":

    user_tasks = requests.get('https://jsonplaceholder.\
typicode.com/users/{}/todos'.format(argv[1])).json()

    username = requests.get('https://jsonplaceholder.typicode.\
com/users?id={}'.format(argv[1])).json()[0]["username"]

    with open('{}.csv'.format(argv[1]), mode="w") as file:
        for task in user_tasks:
            file.write('"{}","{}","{}","{}"\n'.format(task["userId"],
                                                      username,
                                                      task["completed"],
                                                      task["title"]))
