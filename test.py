# import requests

# url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

# headers = {
#     'accept-encoding': "application/gzip",
#     'x-rapidapi-host': "google-translate1.p.rapidapi.com",
#     'x-rapidapi-key': "acfc4a2108msh081da16b8a51692p16dafajsn4803bc7f94ae"
#     }

# response = requests.request("GET", url, headers=headers)

# print(response.text)



# import translators as ts

# wyw_text = 'HEllo my name is hayotbek'
# chs_text = '季姬感到寂寞，罗集了一些鸡来养，鸡是那种出自荆棘丛中的野鸡。野鸡饿了唧唧叫，季姬就拿竹箕中的谷物喂鸡。'
# html_text = '''
# <!DOCTYPE html>
# <html>
# <head>
# 	<title>我是标题</title>
# </head>
# <body>
# <p>我是文章《你的父亲》</p>
# </body>
# </html>
# '''

# # input languages
# print(ts.google(wyw_text)) # default: from_language='auto', to_language='en'

## output language_map
# print(ts._google.language_map)

# professional field
# print(ts.alibaba(wyw_text, professional_field='general')) # ("general","message","offer")
# print(ts.baidu(wyw_text, professional_field='common')) # ('common','medicine','electronics','mechanics')
# print(ts.caiyun(wyw_text, from_language='zh', professional_field=None)) # ("medicine","law","machinery")


# 1-savol
# def s1(students, chairs):
#     return (students-chairs if students > chairs else 0)

# print(s1(25,21))
# print(s1(18,20))
# # output : 4
# # output: 0 


# import random
# # 4-savol
# def s4(item):
#     result_num = 0
    
	

# -*- coding: utf-8 -*-

# from __future__ import unicode_literals

# from djsms import send_text


# frm = '+33123456789'
# to = '+33987654321'
# text = 'Please remember to pick up the bread before coming'
# send_text(text, frm, to)






# from textmagic.rest import TextmagicRestClient
# username = "your_textmagic_username"
# token = "your_apiv2_key"
# client = TextmagicRestClient(username, token)
# message = client.messages.create(phones="9990001001", text="Hello TextMagic")




# from sms import send_sms

# send_sms(
#     'Here is the message',
#     '+12065550100',
#     ['+441134960000'],
#     fail_silently=False
# )





# python script for sending message update

# import time
# from time import sleep
# from sinchsms import SinchSMS

# # function for sending SMS
# def sendSMS():

# 	# enter all the details
# 	# get app_key and app_secret by registering
# 	# a app on sinchSMS
# 	# number = 'your_mobile_number'
# 	# number = '+447520650942'
# 	number = '+998916020335'
# 	app_key = '6b08ec28-fb1c-45ed-b832-d9351cb36fe6'
# 	app_secret = 'RfLi4a1SE0ijcu5Bt8U5UA=='

# 	# enter the message to be sent
# 	message = 'Hello Message!!!'

# 	client = SinchSMS(app_key, app_secret)
# 	print("Sending '%s' to %s" % (message, number))

# 	response = client.send_message(number, message)
# 	message_id = response['messageId']
# 	response = client.check_status(message_id)

# 	# keep trying unless the status returned is Successful
# 	while response['status'] != 'Successful':
# 		print(response['status'])
# 		time.sleep(1)
# 		response = client.check_status(message_id)

# 	print(response['status'])

# if __name__ == "__main__":
# 	sendSMS()


    # id 5b7f8d65ed874228a0070971d3904aa6
    # api_token 7bfa5c19025c479f8abcc2d098a1a6c2
    # url https://us.sms.api.sinch.com/xms/v1
    # service plan id 5b7f8d65ed874228a0070971d3904aa6













    # KEY
    # SHA256:HbW3g8zUjNSksFbqTiUWPWg2Bq1x8xdGUrliXFzSnUw
    # twlio secter xDW3YUB3_NwmTsKNB-qEiXGDZ4PLGmlBDraIFq4J









from crontab import CronTab

cron = CronTab()
job = cron.new(command='python example1.py')
job.minute.every(1)

cron.write()