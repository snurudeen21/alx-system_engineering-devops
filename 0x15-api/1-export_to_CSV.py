#!/usr/bin/python3
""" Extract information using api and
save in CSV file """

import csv
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/{}'.format(url, userId)
    res = requests.get(user)
    json_object = res.json()
    username = json_object.get('username')
    todos = '{}todos?userId={}'.format(url, userId)
    res = requests.get(todos)
    tasks = res.json()

    task_list = []

    for task in tasks:
        task_list.append([userId, username,
                         task.get('completed'),
                         task.get('title')])

    with open('{}.csv'.format(userId), mode='w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in task_list:
            writer.writerow(task)
