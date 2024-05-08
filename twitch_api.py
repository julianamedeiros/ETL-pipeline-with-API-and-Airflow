import requests

#getting a token

client_id='4lm24nqu7lb62cgvcs7gshypus0v4m'
client_secret='4ty1o5vryhxb2twdbzxh8jdnp0fv6r'

url = 'https://id.twitch.tv/oauth2/token'

params = {
    'client_id' : client_id,
    'client_secret' : client_secret,
    'grant_type' : 'client_credentials'

}

response = requests.post(url, params=params)
data = response.json()
print(data)