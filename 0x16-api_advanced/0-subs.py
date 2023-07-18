#!/usr/bin/python3
""" advanced API to return the number
of subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ returns numbers of subreddit
    if found, and 0 if not """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "Toeseen"})
    if response.status_code == 404:
        return 0
    result = response.json()['data']['subscribers']
    return result
