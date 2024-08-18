import schedule
import time
from twilio.rest import Client
import os

# Your Twilio Account SID and Auth Token from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'ACd2982e4e4fa3b83877516bbd1fe3bbe5')
auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'ede6b45fd98433a92084fbc529fd6b28')

# Function to send the WhatsApp message
def send_whatsapp_message():
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello At 15:50 from Pratham',
        to='whatsapp:+919988144169'
    )
    
    print(f"Message sent! SID: {message.sid}")

# Schedule the message to be sent at 3:35 PM
schedule.every().day.at("15:50").do(send_whatsapp_message)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)



