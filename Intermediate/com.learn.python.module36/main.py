import os

import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
VIRTUAL_TWILIO_NUMBER = "+12543183384"
VERIFIED_NUMBER = "+525548238196"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"


API_KEY = os.getenv("API_KEY_ALPHA_VANTAGE")
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY
}
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
print(data)
time_series_daily = [value for (key, value) in data.items()]
yesterday = time_series_daily[0]
print(yesterday)
yesterday_close_price = yesterday["4. close"]
print(yesterday)
day_before_yesterday = time_series_daily[1]
day_before_yesterday_close_price = day_before_yesterday["4. close"]
diferrence_stock_movement = abs(float(day_before_yesterday_close_price) - float(yesterday_close_price))
if diferrence_stock_movement > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
percentage_stock_movement = round((diferrence_stock_movement / float(yesterday_close_price)) * 100, 2)
print(f"{percentage_stock_movement}%")
up_down = None


if percentage_stock_movement > 0:
    API_KEY_NEWS = os.getenv("API_NEWS")
    parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": API_KEY_NEWS
    }
    response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    articles_list = response.json()["articles"]
    three_articles = articles_list[:3]
    print(three_articles)
    formatted_articles = [
        f"{STOCK}: {up_down}{percentage_stock_movement}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in three_articles]
    print(formatted_articles)
    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # TODO 8. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )