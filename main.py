#! /usr/bin/python3
import mal_api
import twitter_api

def main(): 
    top10Tweet = mal_api.generateTop10()
    print(top10Tweet)
    twitter_api.generateTweet(top10Tweet)
    print('Tweeted Successfully')

if __name__ == "__main__":
    main()
