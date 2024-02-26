import requests


API_KEY = "a07b8fe66f0e4c46efe68a0407881c3b"

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={user_input},&appid={API_KEY}")


if weather_data.json(int) ["cod"] =="404":
    print("No City Found: ")
else:
    weather = weather_data.json()["weather"][0]["main"]
    temp = round(weather_data.json()["main"]["temp"])
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is {temp}f")