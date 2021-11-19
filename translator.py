
#  Translation with GOOGLE service
from googletrans import Translator
translator = Translator()
result = translator.translate('Hello World', src='en', dest='uz')

print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)



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