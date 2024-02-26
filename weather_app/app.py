import  datetime as dt
import requests


base_url = "https://api.openweathermap.org/geo/1.0/direct?q"
api_key = "a07b8fe66f0e4c46efe68a0407881c3b"
city = "NEWYORK"

url = base_url + "=" + city + "&appid=" + api_key
response = requests.get(url).json()
print(response)