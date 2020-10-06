import requests # Imports requests library
import os

# For ease, assign API's url to variable "url"
url = f"http://api.openweathermap.org/data/2.5/weather"
key = os.environ.get("WEATHER_KEY")
print(key)

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print("Sorry, could not get weather.")
    else:
        current_temp = get_temp(weather_data)
        print(f"The current temperature is: {current_temp} degrees F")

def get_location():
    city, country = "", ""
    while len(city) == 0:
        city = input("Please enter the city name: ").strip()
    while len(country) == 0:
        country = input("Please enter the two-digit country code: ").strip()
    location = f"{city}, {country}"
    return location

def get_current_weather():
    try:
        query = {"q" : location, "units" : "imperial", "appid" : key}
        response = requests.get(url, params=query)
        response.raise_for_status()
        data = response.json()
        return data, None
    except Exception as e:
        print(e)
        print(response.text)
        return None, e

def get_temp():
    try:
        temp = weather_data["main"]["temp"]
        return temp
    except KeyError:
        print("This data is not in the expected format.")
        return "Unknown"

if __name__ == "__main__":
    main()


city = input("Enter city name: ")
country = input("Enter two-letter country code: ")
location = f"{city}, {country}"
query = {"q" : location, "units" : "imperial", "appid" : key}

data = requests.get(url, params=query).json() # Get API and convert to JSON

temp = data["main"]["temp"]
print(f"The temperature is currently: {temp} degrees F")
