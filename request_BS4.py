import requests
from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
from slugify import slugify
import time

def update_posts():
	r = requests.get("https://kun.uz/news/list")
	soup = BeautifulSoup(r.text, 'html.parser')
	cd_headings = soup.findAll("a", {"class": "daily-block l-item"})

	for th in cd_headings:
		print(' ========================================')
		href = th['href']
		slug = slugify(href)
		post_url = f"https://kun.uz{href}"
		single_r = requests.get(post_url)
		single_soup = BeautifulSoup(single_r.text, 'html.parser')

		view = single_soup.find("div", {"class": "view"}).text
		title = single_soup.find('div', {"class":"single-header__title"}).text	
		body_code = single_soup.find('div', {"class":"single-content"})
		main_img_ls = body_code.findAll('img')
		body = str(body_code)
		
		print('VIEW',view)
		print('TITLE', title)

		print('HREF',href)
		for x in main_img_ls:
			print('Image',x)
		if len(main_img_ls) != 0:
			print('MAIN IMAGE', main_img_ls[0])
	return True

update_posts()