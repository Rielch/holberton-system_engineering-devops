#!/usr/bin/python3
"""Return a list of the titles of all hot posts in a subreddit"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Return  a list of the titles of all
    hot posts in a subreddit recursively"""

    parameters = {"limit": 1}
    parameters["count"] = count
    if after is not None:
        parameters["after"] = after
    r = requests.get("https://www.reddit.com/r/{}/hot.json"
                     .format(subreddit), allow_redirects=False,
                     headers={"User-Agent": "Mozilla/5.0"},
                     params=parameters)
    if r.status_code != 200:
        return None
    after = r.json().get("data").get("after")
    if after is None:
        return hot_list
    count += 1
    hot_list.append([r.json().get("data").get("children")[0]
                     .get("data").get("title")])
    return recurse(subreddit, hot_list, count, after)
