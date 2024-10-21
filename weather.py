from dotenv import load_dotenv
import os
import requests, urllib3

load_dotenv()
api_key = os.getenv("API_KEY")

base_url = "http://api.weatherapi.com/v1"
forecast_url = base_url + "/forecast.json"

params = {
    "key": api_key,
    "q": 94704, # Berkeley ZIP code
    "days": 5,
}

response = requests.get(forecast_url, params=params)

if response.status_code == 200:
    response = response.json()
    location = response["location"]
else:
    print("Unsuccesful forecast request")

print(f"Located in {location["name"]} at: ({location["lat"]}, {location["lon"]})")

print(response["forecast"])
