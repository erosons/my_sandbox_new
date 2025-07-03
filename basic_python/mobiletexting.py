from twilio.rest import Client

account_sid = "AC64ae20d12d0a18784088f536957bf1b7"
auth_token = "e2f1dbbd82564cee8bc74d5702f1f370"

client = Client(account_sid, auth_token)

client.messages.create(
    to="+18326144931", from_="+12563635919", body="Hello wiffy I love you")
