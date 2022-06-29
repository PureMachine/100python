import os
import json
import requests
from datetime import datetime

token = os.environ.get("token")
username = "conrad"
pixela_endpoint = "https://pixe.la/v1/users"

def setup_user():
    params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(pixela_endpoint, json=params)
    j = response.json()
    print(json.dumps(j, indent=4))

def setup_graph():
    params = {
        "name": "yes",
        "id": "a0",
        "unit": "step",
        "type": "int",
        "color": "kuro",
        "timezone": "America/Los_Angeles",
    }
    headers = {"X-USER-TOKEN": token}
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
    response = requests.post(graph_endpoint, json=params, headers=headers)
    j = response.json()
    print(json.dumps(j, indent=4))

def post_steps():
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs/a0"
    date = datetime.now()
    formatted_date = date.strftime("%Y%m%d")
    params = {
        "date": formatted_date,
        "quantity": "10000",
    }
    headers = {"X-USER-TOKEN": token}
    response = requests.post(graph_endpoint, json=params, headers=headers)
    j = response.json()
    print(json.dumps(j, indent=4))


def update_steps(date: str, quantity: str):
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs/a0/{date}"
    params = {
        "quantity": quantity,
    }
    headers = {"X-USER-TOKEN": token}
    response = requests.put(graph_endpoint, json=params, headers=headers)
    j = response.json()
    print(json.dumps(j, indent=4))

def delete_steps(date: str):
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs/a0/{date}"
    headers = {"X-USER-TOKEN": token}
    response = requests.delete(graph_endpoint, headers=headers)
    j = response.json()
    print(json.dumps(j, indent=4))

def main():
    date = datetime.now()
    formatted_date = date.strftime("%Y%m%d")
    delete_steps("20220628")

if __name__ == "__main__":
    main()