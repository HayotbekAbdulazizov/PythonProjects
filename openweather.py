import requests
api_key = '54b9119af7f1b135da4edb201d08fdc6'
r = requests.get("https://api.openweathermap.org/data/2.5/weather?q={london}&appid={54b9119af7f1b135da4edb201d08fdc6}")
print(r)

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
