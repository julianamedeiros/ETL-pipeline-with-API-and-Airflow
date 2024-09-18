import requests
import pandas as pd

#extracting data from the api

client_id = '' #add your credentials
access_token = '' 

def extract(endpoint):
    url =  f'https://api.igdb.com/v4/{endpoint}'
    headers = {
        'Client-ID' : client_id,
        'Authorization' : f'Bearer {access_token}'
    }

    fields = '*'
    data = f'fields {fields}; limit 200;'
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    df = pd.DataFrame(result)
    return df

