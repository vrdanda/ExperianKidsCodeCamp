#
# Google Translate API (Unofficial):
#
# You can use the googletrans Python library (unofficial wrapper for Google Translate) to translate text to French.​

# Remember to replace YOUR_API_KEY with an actual API key if you’re using an official API.
# First, install the library using pip install googletrans==4.0.0-rc1.​
# Then, write code like this:​

from googletrans import Translator

def translate_to_french(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='fr').text
    return translated_text

input_text = "Hello, how are you?"
translated_result = translate_to_french(input_text)
print(f"Translated to French: {translated_result}")


