import requests # Imports requests library
import os

key = os.environ.get("WEATHER_KEY")
print(key)

# For ease, assign API's url to variable "url"
url = f"http://api.openweathermap.org/data/2.5/weather"
city = input("Enter city name: ")
country = input("Enter two-letter country code: ")
location = f"{city}, {country}"
query = {"q" : location, "units" : "imperial", "appid" : key}

data = requests.get(url, params=query).json() # Get API and convert to JSON

temp = data["main"]["temp"]
print(f"The temperature is currently: {temp} degrees F")
