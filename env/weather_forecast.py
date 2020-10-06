import requests
from datetime import datetime
import os
from pprint import pprint


# f"http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&appid=52bf123553b99a8b50aea839f15cd9b5"

key = "52bf123553b99a8b50aea839f15cd9b5"
query = {"q" : "minneapolis,us", "units" : "imperial", "appid" : key}

url = "http://api.openweathermap.org/data/2.5/forecast"

data = requests.get(url, params=query).json()
pprint(data)

forecasts_list = data["list"]

for forecast in forecasts_list:
    temp = forecast["main"]["temp"]
    timestamp = forecast["dt"]
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f"At {forecast_date} the temperature will be {temp} degrees F")

