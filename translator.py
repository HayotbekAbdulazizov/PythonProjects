
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



#


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






# from translation import (set_default_translation, set_default_language,
#     set_default_proxies, get, ConnectError)

# set_default_translation('google')
# set_default_language('auto', 'zh-CN')
# set_default_proxies({'http': 'http://127.0.0.1:1080'})
# try:
#     print(get('hello world!'))
# except ConnectError:
#     print('Invaild proxy')


# from translation import baidu, google, youdao, iciba


# print(google('hello world!', dst = 'ru-RU'))






# from azure_translator import Translator

# t = Translator('your_api_key')
# t.translate('Je suis fatigué')
# 'I am tired'

# >>> t.translate("Hello", to='fr')
# 'Bonjour'

# >>> t.translate("Aujourd'hui", source_language='fr')
# 'Today'
# ``` 



# from translator import Translator
# translator = Translator()

# # translator.load_model(MODEL_PATH)
# translator.translate("What is your name?")  
# आपका नाम क्या है?


# from translator import GoogleTranslator

# # use google
# translator = GoogleTranslator()
# print(translator.translate('我是中国人', dest='en'))

# # use baidu api
# translator = BaiduTranslator(appid, appkey)
# print(translator.translate('我是中国人', dest='en'))

# # use tencent api
# translator = TencentTranslator(appid, appkey)
# print(translator.translate('我是中国人', dest='en'))

# # throttle api call frequency.
# translate_func = throttle(seconds=1)(translator.translate) # call api every second
# for i in range(100):
#   translate_func('我是中国人', dest='en')










# from deep_translator import GoogleTranslator

# proxies_example = {
#     "https": "34.195.196.27:8080",
#     "http": "34.195.196.27:8080"
# }
# translated = GoogleTranslator(source='auto', target='de', proxies=proxies_example).translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig







# DId not tested
# from google_translator_simplified import Translator

#  #'Tekst do tłumaczenia '
# Translator.get_translation('de', 'tekst do przetłumaczenia', 'pl') #'Text für die Übersetzung '
# Translator.get_translation('pl', 'text for translation') #'Tekst do tłumaczenia '
# Translator.get_translation('de', 'tekst do przetłumaczenia') #'Text für die Übersetzung '
# print(Translator.get_translation('pl', 'text for translation', 'en'))



# from gtrans.gtrans import Gtran
# translator = Gtran()
# text = "こんにちは"
# out = translator.translate(text=text)
# print(out)




# from google_trans_new import google_translator  

# translator = google_translator()  
# translate_text = translator.translate('hello',lang_tgt='ru')  
# print(translate_text)





from etranslate import translate
tras = translate("mening ismim hayotbek")  # 'Hello world!'
print(tras)