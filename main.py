# Email Api : devtempmail1+vrctuorntu@gmail.com
## Api Key : 640c80181e6178c89f8002bc0e388b1c

import requests
from requests.models import Response
from dataclasses import dataclass
from typing import Dict

url = "https://api.openweathermap.org/data/2.5/forecast?appid=640c80181e6178c89f8002bc0e388b1c&units=metric&lang=fa&q="
apiKey = "640c80181e6178c89f8002bc0e388b1c"


@dataclass
class WeatherMap:
    day_3hours: list[Dict]

def check_city() -> Response:
    city_name = input("Please Enter Name Of City: ")
    response = requests.get(url + city_name)
    if not city_name:
        print("city name is empty.")
    if response.status_code != 200:
        print(f"can't find your city {city_name}, run again...")
    return response

def get_data_weathermap() -> WeatherMap:
    response = check_city().json()
    total = []
    for data in response['list']:
        result = {}
        result['time'] = data['dt']
        result['temp'] = data['main']['temp']
        result['feels_like'] = data['main']['feels_like']
        result['description'] = data['weather'][0]['description']
        total.append(result)

    weather_data = WeatherMap(total)

    return weather_data
        

if __name__ == '__main__':
    print(get_data_weathermap())
        
        
