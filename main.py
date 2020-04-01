import requests

url = 'http://muslimsalat.com/daily.json'
response = requests.get(url)

print(response, response.json())
