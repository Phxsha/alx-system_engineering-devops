#!/usr/bin/python3
"""gets total number of subs"""


import requests


def get_reddit_token(client_id, client_secret):
    """Handles authentication"""
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {'grant_type': 'client_credentials'}
    headers = {'User-Agent': 'myAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    token = res.json().get('access_token')
    return token


def number_of_subscribers(subreddit, client_id, client_secret):
    """Returns the number of subscribers for a given subreddit"""
    token = get_reddit_token(client_id, client_secret)
    headers = {'Authorization': f'bearer {token}', 'User-Agent': 'myAPI/0.0.1'}
    url = f"https://oauth.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
    return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print(
            "Usage: python3 0-subs.py <subreddit> <client_id> <client_secret>")
    else:
        subreddit = sys.argv[1]
        client_id = sys.argv[2]
        client_secret = sys.argv[3]
        print(number_of_subscribers(subreddit, client_id, client_secret))
