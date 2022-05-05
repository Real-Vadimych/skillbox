from urllib import response
import requests
import pandas as pd

url = 'https://itunes.apple.com/search'
params = {
    'media': 'music',
    'term': 'manizha',
    'limit': 30
    }

response = requests.get(url, params=params)
results = response.json()['results']


print(response.json())