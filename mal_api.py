import keys_test as keys
import requests
from date import currentYear
from date import currWeek
from date import currSeason

def generateTop10(): 
    print(currentYear, currWeek, currSeason)

    url = f"https://api.myanimelist.net/v2/anime/season/{str(currentYear)}/{currSeason}?sort=anime_num_list_users&limit=50&nsfw=true"

    
    response = requests.get(url, headers = {
        'X-MAL-CLIENT-ID': keys.client_id
    }, timeout = 600)

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
            'X-MAL-CLIENT-ID': keys.client_id
        }, timeout = 600)
        anime_data.raise_for_status()
        anime_data_json = anime_data.json()
        anime_data.close() 
    
        if ('mean' not in anime_data_json):
            print(anime_data_json['title'])
            continue

        if(anime_data_json['start_season']['year'] == currentYear) and (anime_data_json['start_season']['season'] == currSeason) and (anime_data_json['media_type'] == 'tv'): 
            print(anime_data_json['title'])
            print(i)
            anime_dict[anime_title] = anime_data_json['mean']

    sorted_by_values = sorted(anime_dict.items(), key=lambda x: -x[1])
    sorted_anime = list(sorted_by_values)
    top10 = []

    for i in range(min(len(sorted_anime), 10)):
        top10.append(sorted_anime[i])

    print(top10)

    capitalSeason = currSeason.capitalize()
    tweet = f"{capitalSeason} {currentYear} Anime Rankings Week {str(currWeek)} \n\n"
    for i in range(min(5, len(top10))):
        tweet = tweet + str(i + 1) + ". " + top10[i][0] + ": " + str(top10[i][1]) + "\n"
    
    return tweet
