import requests
        
# r = requests.get("http://localhost:8080/rendfunc/articles")
# print(r)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))


# url = ('https://newsapi.org/v2/top-headlines?'  'country=us&''apiKey=dfbe32be81974075aba7c153d579c101')
# url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=dfbe32be81974075aba7c153d579c101')

# r = requests.get("http://localhost:8080/admin")

for i in range(300):
    r = requests.get("http://localhost:8080/admin")
    print(r)

#  newsapi.org dfbe32be81974075aba7c153d579c101