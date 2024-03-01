import json
import requests
from requests_oauthlib import OAuth1

# Set up API keys and tokens
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

# OAuth Authentication
auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Function to extract tweet IDs from archived data
def extract_tweet_ids_from_archive(archive_file_path):
    tweet_ids = []
    with open(archive_file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        data = data.replace('window.YTD.tweets.part0 = ', '')
        tweets_data = json.loads(data)

        for tweet in tweets_data:
            tweet_id = tweet['tweet']['id_str']
            tweet_ids.append(tweet_id)
    return tweet_ids

# Function to delete a tweet
def delete_tweets(tweet_ids):
    url_delete_tweet = "https://api.twitter.com/1.1/statuses/destroy/"
    for tweet_id in tweet_ids:
        del_response = requests.post(url_delete_tweet + f"{tweet_id}.json", auth=auth)
        if del_response.status_code == 200:
            print(f"Deleted tweet ID: {tweet_id}")
        else:
            print(f"Failed to delete tweet ID: {tweet_id}, Status Code: {del_response.status_code}")

# execution
archive_file_path = 'tweets-sample.js'  # Specify the path to the archive file
tweet_ids = extract_tweet_ids_from_archive(archive_file_path)
delete_tweets(tweet_ids)
