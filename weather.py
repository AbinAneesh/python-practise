import requests
# API KEY and URL
API_KEY = "d311a0269fd555fefa1590014197c474"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
# retrive data from the server corresponding to the user input city
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather:",weather)
    temperature = round(data['main']['temp']-273.15, 2)
    print("Temperature:",temperature, "celsius")
else:
    print("Error occurred")