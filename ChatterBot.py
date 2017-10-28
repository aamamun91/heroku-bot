# Dependencies
import pandas as pd
import tweepy
import time
import json
import random
import tweepy
import json
import time

# Twitter API Keys
consumer_key = 'SYTnLXrii4S3WlaMlvbQkHXY5'
consumer_secret = 'QhpDbZ8qbB971WTKkQtCtKxC4RN7D4zcjDYIcVO8nMchoKv1fv'
access_token = '866777141567991810-cquWcZc7G9knRgPV5l0ga8s74p4QGfq'
access_token_secret = 'igdaEFPXUswtpN1eCdPs84Aq0LMDCXgU0Fx5BfgO3EuNu'

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]


# Create function for tweeting

def tweetout():
    
    api.update_status(random.choice(happy_quotes))
    
# Twitter credentials

# Tweet a random quote

# Infinite loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    tweetout()

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
     
# Print success message
print("Hey, I did it")

# Set timer to run every minute