#!/usr/bin/python3
"""Retuns the ammount of subsctribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""

    r = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                     allow_redirects=False,
                     headers={"User-Agent": "Mozilla/5.0"})
    return (r.json().get("data").get("subscribers"))
