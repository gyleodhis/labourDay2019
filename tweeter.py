import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = ""
consumer_secret = ""
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('labourDay.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#LabourDay",count=200000,
                           lang="en",
                           since="2019-04-30").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.geo, tweet.retweet_count, tweet.favorite_count, tweet.text.encode('utf-8')])


    #  retweeted in_reply_to_screen_name, name, screen_name,, 