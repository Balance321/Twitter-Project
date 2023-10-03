import keys_test as keys
import tweepy

def generateTweet(tweet): 
    client = tweepy.Client(consumer_key        = keys.api_key_final,
                           consumer_secret     = keys.api_secret_final,
                           access_token        = keys.access_token_final,
                           access_token_secret = keys.access_token_secret_final)

    client.create_tweet(text = tweet)
    # print(tweet) 
