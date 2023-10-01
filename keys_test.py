from turtle import clear
from collections import OrderedDict
import requests
import tweepy

# Twitter
api_key = 'xjP85DKxKG95H8O4Q2tBxx5lP'
api_secret = '7vYbolTHKpCRdbIc6zItRuBbbxp7UF90l701FDysExn2R0nP4w'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAANaNqAEAAAAAA3JBRU6hqnWlOFqUb7Jyb5n4t1g%3D3fzKDwpe94DYkOtcjMKFGZMKrxiEHAoMBmZV9jkJu27U8R5e7W'
access_token = '1706180546878214144-HD7oCzatyJas7yxmGXxZSKP34jbs44'
access_token_secret = 'qDoI3b09duvutIZdDw9mDWizeoaR6cJtp5Db2Nso2mvWD'

api_key_final = 'LrGML5OGXJhjRMONqkoW9UMYp'
api_secret_final = '8zojfEQKlHLp27wq6QtJpsk1XBKjQy65EfW8o48CU7czpvSonB'
bearer_token_final = 'AAAAAAAAAAAAAAAAAAAAAJX5qAEAAAAAFnAg%2FJAa1U63XG%2BZK%2F2FVaKYUPU%3DLNPsqw0DiObjw7FojJDW1CKqDNbtkRrjClqMQIIqwxKEfu0HLx'
access_token_final = '1708287959743815680-onMfErVzHDTxN0hIzSRRzXX0YQ8G9w'
access_token_secret_final = 'tgdOpsmHxugWPEZcVcR73J4I4j395DChhpaTOP664kzqN'

# MAL
client_id = 'adda09f6a4fc2b591f6e65028d31f458'
client_secret = 'f359587358e78986a66d2645cf18a42fade7748936d5cb27a0016c04c7403453'

# url = 'https://api.myanimelist.net/v2/anime/ranking?ranking_type=airing&limit=10'
url = 'https://api.myanimelist.net/v2/anime/season/2023/summer?sort=anime_num_list_users&limit=50&nsfw=true'
response = requests.get(url, headers = {
    'X-MAL-CLIENT-ID': client_id
})

response.raise_for_status()
anime = response.json()
response.close()

anime_id = anime['data'][0]['node']['id']

anime_dict = {}

count = 0
for i in range(50):
    anime_title = anime['data'][i]['node']['title']
    anime_id = anime['data'][i]['node']['id']
    anime_url = 'https://api.myanimelist.net/v2/anime/' + str(anime_id) + '?fields=id,title,main_picture,alternative_titles,start_date,end_date,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,studios,statistics'
    
    anime_data = requests.get(anime_url, headers = {
        'X-MAL-CLIENT-ID': client_id
    })
    anime_data.raise_for_status()
    anime_data_json = anime_data.json()
    anime_data.close() 
    
    if(anime_data_json['start_season']['year'] == 2023) and (anime_data_json['start_season']['season'] == 'summer') and (anime_data_json['media_type'] == 'tv'): 
        print(anime_data_json['title'])
        print(i)
        anime_dict[anime_title] = anime_data_json['mean']

sorted_by_values = sorted(anime_dict.items(), key=lambda x: -x[1])
sorted_anime = list(sorted_by_values)
top_10 = []

for i in range(10):
    top_10.append(sorted_anime[i])

print(top_10)

client = tweepy.Client(consumer_key=api_key_final,
                       consumer_secret=api_secret_final,
                       access_token=access_token_final,
                       access_token_secret=access_token_secret_final)


# Replace the text with whatever you want to Tweet about
tweet = 'Summer 2023 Anime Rankings Week 13 \n\n'
for i in range(5):
    tweet = tweet + str(i + 1) + ". " + top_10[i][0] + ": " + str(top_10[i][1]) + "\n"
    

client.create_tweet(text=tweet)
print(tweet)

# Current data/season
# Schedule tweets for end of the week
# Edge Cases: Anime with no means
# Keep track of the week number
