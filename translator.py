from googletrans import Translator
translator = Translator()
result = translator.translate('Hello World', src='en', dest='uz')

print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)

# nothng 