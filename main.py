import tweepy
import keys_test as keys

client = tweepy.Client(consumer_key=keys.api_key,
                       consumer_secret=keys.api_secret,
                       access_token=keys.access_token,
                       access_token_secret=keys.access_token_secret)

# Replace the text with whatever you want to Tweet about
client.create_tweet(text='this tweet is from my balls')

print('Tweeted Successfully')
