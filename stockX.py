import pip._vendor.requests 
import json 
import tweepy


api_key = 'lxkJgQSMesgiH5upGbQfO6P0z'
api_secret = 'XPhGHubLoqy5MppU4PyuVrAhWbIeKSsUFCnBqOwCTryGXkmsbl'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJBqpwEAAAAAm%2Bu5eHzWiTDgDBhKoUo2o6vOuLA%3DH6VU9k3hxIIBgPD35amub08H9eexQ1B5CdXhE7aZ3DTVbb6VNs'
access_token = '861045267298099200-4HZW3b1qvTr45mqPDXJKGPuL78dKQhk' 
access_token_secret = 'roLGBSUHCC0ihBjJYs28oZ7rckJ8iFLDwD89SOpyE34eP'




client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy(tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret))
api = tweepy.API(auth) 

client.create_tweet(text = "asdjahksdj")