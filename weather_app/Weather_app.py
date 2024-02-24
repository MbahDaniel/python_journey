import requests


API_KEY = "a07b8fe66f0e4c46efe68a0407881c3b"

user_input = input("Enter city: ")

weather_data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_input},&appid={API_KEY}")

if weather_data.json() ["cod"] =="404":
    print("No City Found: ")