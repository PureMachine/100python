import requests
import json

API_KEY = "9817f09d26a9b136d6056dce2e459f61"
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 47.577579
MY_LONG = -122.288078
PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "daily,weekly",
    "appid": API_KEY,
}


response = requests.get(url=BASE_URL, params=PARAMS)
response.raise_for_status()
print(response.status_code)
j = response.json()["hourly"]
weathers = [item["weather"][0]["id"] for item in j[:12]]
# print(json.dumps(j, indent=4))
print(weathers)
need_umbrella = False
for weather in weathers:
    if int(weather) < 700:
        need_umbrella = True

if need_umbrella:
    print("Bring an umbrella")
