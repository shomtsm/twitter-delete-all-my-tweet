import json
import requests
import argparse
import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1

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

# Function to extract liked tweet IDs from archived data
def extract_like_ids_from_archive(archive_file_path):
    tweet_ids = []
    with open(archive_file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        data = data.replace('window.YTD.like.part0 = ', '')
        tweets_data = json.loads(data)

        for tweet in tweets_data:
            tweet_id = tweet['like']['tweetId']
            tweet_ids.append(tweet_id)
    return tweet_ids

# Function to delete tweets
def delete_tweets(tweet_ids):
    url_delete_tweet = "https://api.twitter.com/1.1/statuses/destroy/"
    for tweet_id in tweet_ids:
        del_response = requests.post(url_delete_tweet + f"{tweet_id}.json", auth=auth)
        if del_response.status_code == 200:
            print(f"Deleted tweet ID: {tweet_id}")
        else:
            print(f"Failed to delete tweet ID: {tweet_id}, message: {del_response.status_code}")

# Function to unlike tweets
def unlike_tweets(tweet_ids):
    url_delete_tweet = "https://api.twitter.com/1.1/favorites/destroy/"
    for tweet_id in tweet_ids:
        del_response = requests.post(url_delete_tweet + f"{tweet_id}.json", auth=auth)
        if del_response.status_code == 200:
            print(f"Unliked tweet ID: {tweet_id}")
        else:
            print(f"Failed to unlike tweet ID: {tweet_id}, message: {del_response.text}")

# Parse file argument
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

# Set up API keys and tokens
load_dotenv()
API_KEY=os.getenv("API_KEY")
API_SECRET_KEY=os.getenv("API_SECRET_KEY")
ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET=os.getenv("ACCESS_TOKEN_SECRET")

# OAuth Authentication
auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# execution
if args.filename.endswith('tweets.js'):
    tweet_ids = extract_tweet_ids_from_archive(args.filename)
    delete_tweets(tweet_ids)
elif args.filename.endswith('like.js'):
    tweet_ids = extract_like_ids_from_archive(args.filename)
    unlike_tweets(tweet_ids)
else:
    print('Unrecognized file!')