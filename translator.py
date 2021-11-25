
#  Translation with GOOGLE service
# from googletrans import Translator
# translator = Translator()
# result = translator.translate('Hello World', src='en', dest='uz')

# print(result.src)
# print(result.dest)
# print(result.origin)
# print(result.text)
# print(result.pronunciation)



# Translation with YANDEX service
def traslate(text, key):
    lang = 'en'
    url_yandex ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&text=%s&lang=%s" % (key,text,lang)
    time.sleep(0.3)
    response = requests.get(url_yandex, timeout=None)
    response_data = eval(response.content.decode('utf-8'))
    lb = response_data['text'][0]
    return lb
#  9860 0301 7424 1627shaxriyor xamdanjonov
 
#Test function
text = 'Hola Mundo!'
key = 'APIKEY' #insert apikey in https://tech.yandex.com/translate/
# traslate(text, key)
#'Hello World!'





# import requests

# url = "https://sa-translate.p.rapidapi.com/translate/html/text"

# payload = "{\"url\":\"http://snjassociates.net/journal-articles/\",\"sourceLanguage\":\"english\",\"targetLanguage\":\"de\"}"
# headers = {
#     'content-type': "application/json",
#     'x-rapidapi-host': "sa-translate.p.rapidapi.com",
#     'x-rapidapi-key': "acfc4a2108msh081da16b8a51692p16dafajsn4803bc7f94ae"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)






# import requests
# # https://www.translated.net/hts/?f=quote&cid=htsdemo&p=htsdemo5&s=english&t=italian&w=1000&of=json

# response = requests.get('https://www.translated.net/hts/?f=quote&cid=htsdemo&p=htsdemo5&s=english&t=italian&w=1000&of=json')
# print(response)
# print(response.text)



import requests
req = requests.post(
    'https://libretranslate.com/translate',
    { 
        'body':{
            'q':'hello',
            'source':'en',
            'target':'ru'
        },
                                                })

print(req)
print(req.text)



# const res = await fetch("https://libretranslate.com/translate", {
# 	method: "POST",
# 	body: JSON.stringify({
# 		q: "Hello!",
# 		source: "en",
# 		target: "es"
# 	}),
# 	headers: { "Content-Type": "application/json" }
# });

# console.log(await res.json());

