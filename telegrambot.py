		

import telebot
bot = telebot.TeleBot('2018620537:AAFRlA6ilkvL2g2guN0_0OWpY-eNgWecOQo')
channel_id = '@world_news_on'
group_id = -472794572

# bot.send_photo(
	# parse_mode='HTML',
	# chat_id=channel_id, 
	# photo=main_im, 
	# caption=f' <b> {title} </b>  \n   {str(paragraphs[0].text) } \n \n  {tg_link} ')
	
bot.send_video(chat_id=channel_id, video=open('shoton.mp4', 'rb'), supports_streaming=True)