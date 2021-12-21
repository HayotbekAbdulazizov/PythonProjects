"""
        This module hepls us to send sms or make phone calls from virtual number given from twilio 
"""
## account-sid = AC7aa8bffd8a84b62268925d7bf61463ec
## auth-token = 6101ed8df69c7df4d581cd0b06374fa7
## phone-number = +13143250938
## Twilio-account = hayotbekabdulazizovdev@gmail.com
## passoword = gafur22hayotbek
## active-number = +998916020335

# from twilio.rest import Client

# account_sid = 'AC7aa8bffd8a84b62268925d7bf61463ec'
# auth_token = '6101ed8df69c7df4d581cd0b06374fa7'

# client = Client(account_sid, auth_token)
# def send_sms( body , to='+998916020335', from_='+13143250938'):
#     client.messages.create(from_=from_ , body=body , to=to)
#     return True
# send_sms('qale ishkar')    




# from twilio.cli import Client
# import os

# from twilio.rest import Client

# account_sid = 'AC7aa8bffd8a84b62268925d7bf61463ec'
# auth_token = '6101ed8df69c7df4d581cd0b06374fa7'
#     # media_url='https://demo.vehica.com/user/emily/',
 
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     body='hello this is mms',
#     from_='+13143250938',
#     to='+998916020335'
# )
# print(message.sid)


# import twilio
# from twilio.rest import Client
# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = 'AC7aa8bffd8a84b62268925d7bf61463ec'
# auth_token = '6101ed8df69c7df4d581cd0b06374fa7'
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15017122661',
#                      to='+15558675310'
# )

# print(message.sid)




import os
from twilio.rest import Client


# Find your Accouhonnt SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACabc07fd87667af0f9f1d3621754c6056'
auth_token = '96420ab5a1a6deba37b686b9332b190e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13143250938',
                     to='+998916020335'
                 )

print(message.sid)


