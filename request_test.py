import requests
from bs4 import BeautifulSoup

def schedule_api():
    # r = requests.get("https://www.instagram.com/militsiya_102/")
    r = requests.get("https://www.instagram.com/p/CWplJV4jWlD/")
    soup = BeautifulSoup(r.text, 'html.parser')
        # view = single_soup.find("div", {"class": "view"}).text
        # title = single_soup.find('div', {"class":"single-header__title"}).text	
        # body_code = single_soup.find('div', {"class":"single-content"})
    print(soup)
        # main_img_ls = body_code.findAll('img')



schedule_api()





# url = 'http://localhost:8080/api/category/'
# r = requests.get(url)
# print(r.text)
# print(type(r.text))