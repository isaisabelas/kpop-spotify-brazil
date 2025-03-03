# Filter the groups popularity in Brazil: 
# Look for each groups' top tracks in Brazil and use their popularity as reference 

import requests
from get_spotify_token import get_token
from get_kpop_groups import kpop_groups
import json

def get_popularity_in_brazil(artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    params = {"market": "BR"}
    headers = {"Authorization": f"Bearer {get_token()}"}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    tracks = response.json()["tracks"]

    if tracks: 
        avg_popularity = sum(track["popularity"] for track in tracks) / len(tracks)
        return avg_popularity
    else:
        return 0  # If the artist has no tracks in Brazil, return 0
    
kpop_popularity_br = []
    
for group in kpop_groups["artists"]["items"]:
    artist_id = group["id"]
    popularity = get_popularity_in_brazil(artist_id)
    kpop_popularity_br.append({"name": group["name"], "popularity": popularity})
        
kpop_popularity_br.sort(key=lambda group: group["popularity"], reverse=True)
    
print("\nGrupos de K-pop mais populares no Brasil:")
for group in kpop_popularity_br[:10]:  # Top 10
    print(f"{group['name']} - Popularidade média no Brasil: {group['popularity']}")
    
with open("kpop_popularity_br.json", "w") as file:
    json.dump(kpop_popularity_br, file, indent=4)

print("\nGrupos de K-pop mais populares no Brasil salvos em kpop_popularity_br.json")
# The code above will save the 10 most popular K-pop groups in Brazil in a file called kpop_popularity_br.json