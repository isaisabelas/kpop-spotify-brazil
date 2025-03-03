# Filter the 50 most popular kpop groups

import requests 
from get_spotify_token import get_token
import json

def search_kpop_groups():
    url = "https://api.spotify.com/v1/search"
    params = {
        "q": "kpop",
        "type": "artist",
        "limit": 50
    }
    
    headers = {"Authorization": f"Bearer {get_token()}"}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

kpop_groups = search_kpop_groups()

for group in kpop_groups["artists"]["items"]:
    print(f"{group['name']} - Popularidade: {group['popularity']}")

with open("kpop_groups.json", "w") as file:
    json.dump(kpop_groups, file, indent=4)
    
print("Grupos de K-pop salvos em kpop_groups.json")
# The code above will save the 50 most popular K-pop groups in a file called kpop_groups.json