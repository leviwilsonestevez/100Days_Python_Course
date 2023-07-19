import os

from twilio.rest import Client

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
VIRTUAL_TWILIO_NUMBER = "+12543183384"
VERIFIED_NUMBER = "+525548238196"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
