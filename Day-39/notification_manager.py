from twilio.rest import Client

TWILIO_SID = "AC636f6c2d70b7af89d802073efa1dc383"
TWILIO_AUTH_TOKEN = "a5e16c13cdbb25a604080ef8d1a96ead"
TWILIO_VIRTUAL_NUMBER = '+12566188877'
TWILIO_VERIFIED_NUMBER = '+919035932042'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)