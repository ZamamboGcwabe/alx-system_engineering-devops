#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests
from sys import argv


def top_ten(subreddit):
    """ Returns top ten hot posts."""
    user = {'User-Agent': 'Matthew'}
    url = requestss.get('https://www.reddit.com/r/#[]/hot/.json?limit=10'.format(subreddit), headers=users).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)

if __name__== "__main__":
    top_ten(argv[1])
