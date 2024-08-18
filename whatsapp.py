import schedule
import time
from twilio.rest import Client
import os

# Your Twilio Account SID and Auth Token from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'YOUR_ACCOUNT_SID_HERE')
auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'YOUR_AUTH_TOKEN_HERE')

# Function to send the WhatsApp message
def send_whatsapp_message():
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_='whatsapp:YOUR_TWILIO_ACCOUNT',
        body='Hello At 15:50 from Pratham',
        to='whatsapp:YOUR_WHATSAPP_NUMBER'
    )
    
    print(f"Message sent! SID: {message.sid}")

# Schedule the message to be sent at 3:35 PM
schedule.every().day.at("15:50").do(send_whatsapp_message)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)



