import urllib.request 
import json 

#url to get frequently played games... sounds kind of interesting
# we can try and predict the games that this person will purchase next 
# we can also try and predict or recommend a set of users to play with 
#    
base_url = 'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key='
# enter the api key 
api_key = 'A6B424B257F21D0C9BFD54CE2C967591'
# enter the user id for which to find recently played games
steam_id='76561197960434622'

resp_format='json'

api_url = base_url + api_key +'&steamid=' + steam_id + '&format=' + resp_format


with urllib.request.urlopen(api_url) as response:
	str_response = response.readall().decode('utf-8')
	user_data = json.loads(str_response)

print(json.dumps(user_data, sort_keys=True, indent=4))

