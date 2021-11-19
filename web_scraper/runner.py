from bs4.element import CData
import requests
from bs4 import BeautifulSoup
from slugify import slugify
from tg_bot import CreatePage, bot, channel_id
import time




# # Main Post-Updater

# r = requests.get("https://kun.uz/news/list")
# soup = BeautifulSoup(r.text, 'html.parser')
# cd_headings = soup.findAll("a", {"class": "daily-block l-item"})
# print(len(cd_headings))
# # for i in cd_headings:
#     # print('=========' , i['href'])
# for th in cd_headings:
#     href = th['href']
#     slug = slugify(href)
#     post_url = f"https://kun.uz{href}"
#     single_r = requests.get(post_url)
#     single_soup = BeautifulSoup(single_r.text, 'html.parser')
#     view = single_soup.find("div", {"class": "view"}).text
#     title = single_soup.find('div', {"class":"single-header__title"}).text	
#     body_code = single_soup.find('div', {"class":"single-content"})
#     main_img_ls = body_code.findAll('img')
#     paragraphs = body_code.findAll('p')
#     main_img = ''
#     if len(main_img_ls) != 0:
#         main_img = main_img_ls[0]['src']
#     else:
#         main_img = 'https://storage.kun.uz/source/thumbnails/_medium/7/L88XGffdJ2B1z7VmOZQTVboR-FMgL2mP_medium.jpg'
#     body = str(body_code)
#     print('VIEW',view)
#     print('TITLE', title)
#     print('HREF',href)
#     tg_link = CreatePage(title, body_code)
#     print(tg_link)
#     print(title)
#     bot.send_photo(
#     parse_mode='HTML',
#     chat_id=channel_id, 
#     photo=main_img , 
#     caption=f' <b> {title} </b>  \n   {str(paragraphs[0].text) } \n \n  {tg_link}    ')
#     time.sleep(2)
        
def schedule_api():
	r = requests.get("https://kun.uz/news/list")
	soup = BeautifulSoup(r.text, 'html.parser')
	cd_headings = soup.findAll("a", {"class": "daily-block l-item"})
	for th in soup.findAll("a", {"class": "daily-block l-item"}):
		href = th['href']
		slug = slugify(href)
		post_url = f"https://kun.uz{href}"
		single_r = requests.get(post_url)
		single_soup = BeautifulSoup(single_r.text, 'html.parser')
		view = single_soup.find("div", {"class": "view"}).text
		title = single_soup.find('div', {"class":"single-header__title"}).text	
		body_code = single_soup.find('div', {"class":"single-content"})

		main_img_ls = body_code.findAll('img')
		paragraphs = body_code.findAll('p')

		main_img = ''

		if len(main_img_ls) != 0:
			main_img = main_img_ls[0]['src']
		else:
			main_img = 'https://storage.kun.uz/source/thumbnails/_medium/7/L88XGffdJ2B1z7VmOZQTVboR-FMgL2mP_medium.jpg'

		body = str(body_code)


		# try:
			# Post.objects.get(slug=slug)
		# except:
			# Post.objects.create(slug=slug)
		# finally:
		tg_link = CreatePage(title, body_code)
		bot.send_photo(
		parse_mode='HTML',
		chat_id=channel_id, 
		photo=main_img , 
		caption=f' <b> {title} </b>  \n   {str(paragraphs[0].text) } \n \n  {tg_link} ')
			
		return True
schedule_api()
