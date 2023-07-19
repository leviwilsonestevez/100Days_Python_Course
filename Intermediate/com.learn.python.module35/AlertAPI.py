import requests
from twilio.rest import Client

api_key = ""

account_sid: str = ""
auth_token: str = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hi soy tu levis. Este es mi primer SMS enviando por Phyton',
    from_='+12543183384',
    to='+525548238196'
)

print(message.sid)
weather_params = {
    "lat": 19.622371,
    "lon": -99.138262,
    "appid": api_key

}
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(url=OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()
print(data["weather"])
