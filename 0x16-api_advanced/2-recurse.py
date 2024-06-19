#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    # Define the URL and headers
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-app:v1.0.0 (by /u/your_username)'}
    params = {'after': after, 'limit': 100}

    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check for a valid response
        if response.status_code == 200:
            data = response.json()
            articles = data['data']['children']
            
            # Add titles to the hot_list
            for article in articles:
                hot_list.append(article['data']['title'])
            
            # Check if there is another page of results
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            # Invalid subreddit or other error
            return None
    except requests.RequestException:
        # Handle network errors
        return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
