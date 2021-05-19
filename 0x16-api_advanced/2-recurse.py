#!/usr/bin/python3
"""Return a list of the titles of all hot posts in a subreddit"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Return  a list of the titles of all
    hot posts in a subreddit recursively"""

    if after != None:
        if after == "STOP":
            return hot_list
    r = requests.get("https://www.reddit.com/r/{}/hot.json\
?count={:d}&after={}&limit=1"
                     .format(subreddit, count, after), allow_redirects=False,
                     headers={"User-Agent": "Mozilla/5.0"})
    if r.status_code != 200:
        return None
    count += 1
    after = r.json().get("data").get("after", "STOP")
    if not after:
        after = "STOP"
    hot_list.append([r.json().get("data").get("children")[0]
                     .get("data").get("title")])
    hot_list = recurse(subreddit, hot_list, count, after)
    return hot_list
