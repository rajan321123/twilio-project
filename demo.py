






import twilio
from twilio.rest import Client
mono=["enter reciever's number"]

# Your Account SID from twilio.com/console
account_sid = "enter your sid"
# Your Auth Token from twilio.com/console
auth_token  = "enter your token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=mono[0], 
    from_="enter your twilio number",
    body="hello this is Rajan Mishra and i send message by using python")

print(message.sid)
