import time
from datetime import datetime as dt
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_pos = {
    "lat": float(response.json()["iss_position"]["latitude"]),
    "lng": float(response.json()["iss_position"]["longitude"]),
}

my_pos = {
    "lat": 47.577579,
    "lng": -122.288078,
}

test_pos = {
    "lat": iss_pos["lat"]+5,
    "lng": iss_pos["lat"]-5,
}

params = {
    "lat": iss_pos["lat"],
    "lng": iss_pos["lng"],
    "formatted": 0,
}


def within_range(viewer, viewing):
    if viewer["lat"] - viewing["lat"] <= 5 and viewer["lng"] - viewing["lng"] <= 5:
        return True
    return False


def send_email():
    pass


response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

data = response.json()["results"]
sunrise_hour = int(data["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["sunset"].split("T")[1].split(":")[0])
now = dt.now().hour

while True:
    if within_range(my_pos, iss_pos) and now > sunset_hour:
        send_email()
        print("look up!")
    time.sleep(60)

