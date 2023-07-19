import os

import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_NAME = "leviwilson"
GRAPH_NAME = "graph20230524"
body = {
    "token": os.environ.get("API_PIXELA_KEY"),
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=PIXELA_ENDPOINT, json=body)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_NAME,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers_auth = {
    "X-USER-TOKEN": os.environ.get("API_PIXELA_KEY")
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers_auth)
# print(response.text)

pixel_creaction_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_NAME}"
today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "9.74"
}
# response = requests.post(url=pixel_creaction_endpoint, json=pixel_data, headers=headers_auth)
# print(response.text)

update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_NAME}/{today}"

new_pixel_data = {
    "quantity": "12.7"
}

response = requests.put(url=update_pixel_endpoint, json=new_pixel_data, headers=headers_auth)
print(response.text)

delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_NAME}/{today}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers_auth)
print(response.text)
