import requests
import requests

# url = 'http://localhost:8080/api/category/'
# r = requests.get(url)
# print(r.text)
# print(type(r.text))


url = 'http://localhost:8080/api/category/'
r = requests.post(url, data={'status':400})