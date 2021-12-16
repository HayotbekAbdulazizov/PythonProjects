# import requests

# url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

# headers = {
#     'accept-encoding': "application/gzip",
#     'x-rapidapi-host': "google-translate1.p.rapidapi.com",
#     'x-rapidapi-key': "acfc4a2108msh081da16b8a51692p16dafajsn4803bc7f94ae"
#     }

# response = requests.request("GET", url, headers=headers)

# print(response.text)



import translators as ts

wyw_text = 'HEllo my name is hayotbek'
chs_text = '季姬感到寂寞，罗集了一些鸡来养，鸡是那种出自荆棘丛中的野鸡。野鸡饿了唧唧叫，季姬就拿竹箕中的谷物喂鸡。'
html_text = '''
<!DOCTYPE html>
<html>
<head>
	<title>我是标题</title>
</head>
<body>
<p>我是文章《你的父亲》</p>
</body>
</html>
'''

# input languages
print(ts.google(wyw_text)) # default: from_language='auto', to_language='en'

## output language_map
# print(ts._google.language_map)

# professional field
print(ts.alibaba(wyw_text, professional_field='general')) # ("general","message","offer")
# print(ts.baidu(wyw_text, professional_field='common')) # ('common','medicine','electronics','mechanics')
# print(ts.caiyun(wyw_text, from_language='zh', professional_field=None)) # ("medicine","law","machinery")
