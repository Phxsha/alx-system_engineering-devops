#!/usr/bin/python3

"""
Module for querying the Reddit API to get the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'python:reddit.project:v1.0 (by /u/yourapp)'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print("None")
    except requests.RequestException:
        print("None")
