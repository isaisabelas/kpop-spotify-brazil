import requests #The requests module allows you to send HTTp requests using Python
import base64 #The base64 module provides a function to encode the credentials in base64

CLIENT_ID = "c4cc687dff974a36aed512412e9817b3"
CLIENT_SECRET = "b0aaaf4d30c3430e9c442f9db21aa3b5"

def get_token():
    url='https://accounts.spotify.com/api/token'
    headers = { 
                'Authorization': 'Basic ' + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
                'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = { 'grant_type': 'client_credentials' }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # This will raise an error for bad responses
    return response.json()["access_token"]

TOKEN = get_token()
print(TOKEN) #Token expires in 1 hour 