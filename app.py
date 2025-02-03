import requests
from twilio.rest import Client
import time
import os
from dotenv import load_dotenv  # Import the load_dotenv function

# Load environment variables from .env file
load_dotenv()

# Get environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")
ENDPOINT_URL = os.getenv("ENDPOINT_URL")

# Global variable to track API status
api_was_down = False

def check_endpoint_availability(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking endpoint: {e}")
        return False

def send_sms_notification(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
        print(f"SMS sent: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

def main():
    global api_was_down

    while True:
        if check_endpoint_availability(ENDPOINT_URL):
            print("Endpoint is available.")
            if api_was_down:
                # Notify that the API is back online
                send_sms_notification("Alert: The endpoint is back online!")
                api_was_down = False  # Reset the flag
        else:
            print("Endpoint is not available.")
            if not api_was_down:
                # Notify that the API is down
                # send_sms_notification("Alert: The endpoint is not available!")
                api_was_down = True  # Set the flag

        # Wait for 5 minutes before checking again
        time.sleep(300)  # 300 seconds = 5 minutes

if __name__ == "__main__":
    main()