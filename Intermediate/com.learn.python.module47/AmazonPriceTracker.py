import bs4
import requests
import lxml
from bs4 import BeautifulSoup
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

URL = "https://www.amazon.com/-/es/REV2-0-ventiladores-WINDFORCE-GV-N3060EAGLE-OC-12GD/dp/B0971B5B1L/ref=sr_1_3?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=S7XHBVHLO2HM&keywords=gtx+3060&qid=1686109777&sprefix=gtx+3060%2Caps%2C128&sr=8-3"
headers_auth = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37",
    "Accept-Language": "es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5"
}
response = requests.get(url=URL, headers=headers_auth)

soup = bs4.BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
print(price)
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 2000
SCOPES = [
    "https://www.googleapis.com/auth/gmail.send"
]

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    flow = InstalledAppFlow.from_client_secrets_file('C:/Users/Levis Wilson/credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=creds)
    body_message = f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
    message = MIMEText(body_message)
    message['to'] = 'leviwilsonestevez2013@gmail.com'
    message['subject'] = 'Amazon Price Alert'
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(f"sent message to {message} Message Id: {message['id']}")
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None
