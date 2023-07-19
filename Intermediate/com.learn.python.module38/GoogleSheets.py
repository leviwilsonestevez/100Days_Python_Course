from datetime import datetime

import requests

APP_ID = "e3f08f5b"
API_KEY = "32af52bf02f35cb68aeb290b6ed68380"

URL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = "https://api.sheety.co/aeb1591f06cb7a8efe02d5d69255043d/myWorkoutsLevisWilson/workouts"
hearders_auth = {
    "Authorization": "Bearer dstweq45647245gfhzdhgdk4i935754265432642376snyetu46356shy783463",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}

body = {
    "query": "ran 3 miles",
    "gender": "male",
    "weight_kg": 96.0,
    "height_cm": 174.64,
    "age": 32
}
response = requests.post(url=URL_ENDPOINT, json=body, headers=hearders_auth)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
