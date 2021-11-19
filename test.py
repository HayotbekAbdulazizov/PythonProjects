import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "acfc4a2108msh081da16b8a51692p16dafajsn4803bc7f94ae"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)