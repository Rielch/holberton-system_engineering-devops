#!/usr/bin/python3
"""prints the titles of the top ten posts of a given subreddit"""
import requests


def top_ten(subreddit):
    """prints the titles of the top ten posts of a given subreddit"""

    r = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                     .format(subreddit),
                     allow_redirects=False,
                     headers={"User-Agent": "Mozilla/5.0"})
    if r.status_code != 200:
        print(None)
    else:
        for post in r.json().get("data").get("children"):
            print(post.get("data").get("title"))
