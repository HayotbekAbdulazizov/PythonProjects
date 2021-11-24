import requests
import requests

# url = 'http://localhost:8080/api/category/'
# r = requests.get(url)
# print(r.text)
# print(type(r.text))


url = 'http://localhost:8080/api/category/'
r = requests.post(url, data={'status':400})

request.get('https://instagram.com')





# def schedule_api():
#     r = requests.get("https://www.instagram.com/militsiya_102/")
#     soup = BeautifulSoup(r.text, 'html.parser')
#         # view = single_soup.find("div", {"class": "view"}).text
#         # title = single_soup.find('div', {"class":"single-header__title"}).text	
#         # body_code = single_soup.find('div', {"class":"single-content"})
#     print(soup)
#         # main_img_ls = body_code.findAll('img')



# schedule_api()