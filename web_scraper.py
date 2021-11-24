# import requests
# from django.shortcuts import redirect, render
# from bs4 import BeautifulSoup
# from slugify import slugify
# import time

# def update_posts():
# 	r = requests.get("https://kun.uz/news/list")
# 	soup = BeautifulSoup(r.text, 'html.parser')
# 	cd_headings = soup.findAll("a", {"class": "daily-block l-item"})

# 	for th in cd_headings:
# 		print(' ========================================')
# 		href = th['href']
# 		slug = slugify(href)
# 		post_url = f"https://kun.uz{href}"
# 		single_r = requests.get(post_url)
# 		single_soup = BeautifulSoup(single_r.text, 'html.parser')

# 		view = single_soup.find("div", {"class": "view"}).text
# 		title = single_soup.find('div', {"class":"single-header__title"}).text	
# 		body_code = single_soup.find('div', {"class":"single-content"})
# 		main_img_ls = body_code.findAll('img')
# 		body = str(body_code)
		
# 		print('VIEW',view)
# 		print('TITLE', title)

# 		print('HREF',href)
# 		for x in main_img_ls:
# 			print('Image',x)
# 		if len(main_img_ls) != 0:
# 			print('MAIN IMAGE', main_img_ls[0])
# 	return True

# update_posts()


# def translate_to_latin(text):
# 	symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯҳҲқ ",
#     (*list(u'abvgdee'), 'j', *list(u'zijklmnoprstuf'), 'kh', 'z', 'ch', 'sh', 'sh', '',
#     'y', '', 'e', 'yu','ya', *list(u'ABVGDEE'), 'J', 
#     *list(u'ZIJKLMNOPRSTUF'), 'KH', 'Z', 'CH', 'SH', 'SH', *list(u'_Y_E'), 'YU', 'YA','x' ,'X' , 'q',' '))

# 	coding_dict = {source: dest for source, dest in zip(*symbols)}
# 	result = ''.join([coding_dict[i] for i in text else pass])
# 	return result











# Testing Translation
from googletrans import Translator
import requests
from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
from slugify import slugify
import time
from transliterate import to_latin

translator = Translator()
# translator.translate('안녕하세요.')

def update_posts():
	r = requests.get("https://kun.uz/news/list")
	soup = BeautifulSoup(r.text, 'html.parser')
	cd_headings = soup.findAll("a", {"class": "daily-block l-item"})

	for th in cd_headings[:3]:
		print(' ========================================')
		href = th['href']
		slug = slugify(href)
		post_url = f"https://kun.uz{href}"
		single_r = requests.get(post_url)
		single_soup = BeautifulSoup(single_r.text, 'html.parser')
		# print(single_soup.get_text())    # this is to get only text
		view = single_soup.find("div", {"class": "view"}).text
		title = single_soup.find('div', {"class":"single-header__title"}).text	
		body_code = single_soup.find('div', {"class":"single-content"})
		main_img_ls = body_code.findAll('img')
		body = str(body_code)
		
		print('VIEW',view)
		# print('TITLE', translator.translate(latin_title, dest='en', src='uz'))
		latin_title = to_latin(title)
		print('TITLE', translator.translate(latin_title, src='uz', dest='ru').text)
		print('POST_URL', post_url)
		print('HREF',href)
		for x in main_img_ls:
			print('Image',x)
		if len(main_img_ls) != 0:
			print('MAIN IMAGE', main_img_ls[0])
		time.sleep(1)	
	return True

update_posts()