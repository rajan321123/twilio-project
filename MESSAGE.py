#!/usr/bin/env python
# coding: utf-8

# In[3]:


import yagmail
from twilio.rest import Client
import pywhatkit as kit

# Function to send WhatsApp message
def send_whatsapp_message():
    phone_number = input("Enter the recipient's phone number (with country code): ")
    message = input("Enter the message you want to send: ")
    kit.sendwhatmsg(phone_number, message, 23, 33)

# Function to send an email
def send_email():
    sender_email = input("Enter your email address: ")
    receiver_email = input("Enter the recipient's email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")
    
    # You should replace 'your_email@gmail.com' and 'your_password' with your actual email and app password
    yag = yagmail.SMTP(sender_email, 'qyvy tlto ptwp hnju')
    yag.send(receiver_email, subject, body)

# Function to send an SMS using Twilio
def send_sms():
    account_sid = 'account_sid'
    auth_token ='auth_token' 
    client = Client( account_sid, auth_token )
    
    from_phone = input("Enter your Twilio phone number (including country code): ")
    to_phone = input("Enter the recipient's phone number (including country code): ")
    message = input("Enter the SMS message you want to send: ")
    
    message = client.messages.create(
        body=message,
        from_=from_phone,
        to=to_phone
    )

# Main program loop
while True:
    print("Choose an option:")
    print("1. Send WhatsApp message")
    print("2. Send Email")
    print("3. Send SMS")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        send_whatsapp_message()
    elif choice == '2':
        send_email()
    elif choice == '3':
        send_sms()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose a valid option.")


# In[ ]:





# In[ ]:





# In[ ]:




