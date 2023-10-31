import requests
import pandas as pd

baseurl = "https://rickandmortyapi.com/api/"
endpoint = 'character'

def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    CharacterList = []
    for item in response['results']:
        character = {
            'id': item['id'],
            'name': item['name'], 'number_ep': len(item['episode']),
        }
        CharacterList.append(character)
    return CharacterList
    
CharacterList = []

data = main_request(baseurl, endpoint, 1)
for x in range(1, get_pages(data)+1):
    print(x)
    CharacterList.extend(parse_json(main_request(baseurl, endpoint, x)))

df = pd.DataFrame(CharacterList)
df.to_csv('RandMCharacterlist.csv', index=False)
