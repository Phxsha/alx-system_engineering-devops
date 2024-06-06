#!/usr/bin/python3
"""Task query reddit API"""


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


def recurse(subreddit, hot_list=[], after=None):
    """retreives the hottest articles"""
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    token = get_reddit_token(client_id, client_secret)
    headers = {'Authorization': f'bearer {token}', 'User-Agent': 'myAPI/0.0.1'}

    url = f'https://oauth.reddit.com/r/{subreddit}/hot'
    params = {'limit': 100}
    if after:
        params['after'] = after

    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        data = res.json().get('data')
        if not data:
            return hot_list if hot_list else None

        children = data.get('children', [])
        for child in children:
            hot_list.append(child.get('data').get('title'))

        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


def count_words(subreddit, word_list, word_count={}):
    """Counts the occurrence of keywords in hot articles"""
    if not word_list:
        # Sort the dictionary by count and then by word
        sorted_word_count = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
        return

    word = word_list.pop(0).lower()
    if word not in word_count:
        word_count[word] = 0

    hot_list = recurse(subreddit)
    if hot_list:
        for title in hot_list:
            words = title.lower().split()
            word_count[word] += words.count(word)
    count_words(subreddit, word_list, word_count)


if __name__ == '__main__':
    count_words(sys.argv[1], sys.argv[2:])
