#!/usr/bin/python3
""" get a top ten hot post """
import requests


def top_ten(subreddit):
    """ return top 10 posts
    or return 0 if none is found"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers={"user-agent": "Toeseen"},
                       params={"limit": 10}, allow_redirects=False)
    result = res.json().get("data")
    try:
        for i in result.get("children"):
            print(i.get('data').get('title'))
    except Exception as err:
        print("None")
