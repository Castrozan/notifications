import requests
from twilio.rest import Client
import time
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")
ENDPOINT_URL = os.getenv("ENDPOINT_URL")

api_was_down = True  # Start as True to avoid initial notification

def check_endpoint_availability(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

def send_sms_notification(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
    except Exception as e:
        print(f"Error sending SMS: {e}")

def main():
    global api_was_down

    while True:
        if check_endpoint_availability(ENDPOINT_URL):
            print("Endpoint is available.")
            if api_was_down:
                send_sms_notification("Alert: The endpoint is back online!")
                api_was_down = False
        else:
            print("Endpoint is not available.")
            api_was_down = True

        time.sleep(300)

if __name__ == "__main__":
    main()