from googletrans import Translator as TranslatorGoogle
from deepl import Translator as TranslatorDeepL
from config import apiKeyDeepL

# Google translate
def translateGoogle(text, destinationLanguage):
    translatorGoogle = TranslatorGoogle()
    try:
        if destinationLanguage == "en": 
            translation = translatorGoogle.translate(text)
        else:
            translation = translatorGoogle.translate(text, dest=destinationLanguage)
    except:
        translation = ""
        print("Probably unsupported language symbol. No translation possible")
    return translation.text

# DeepL translate
def translateDeepL(text, destinationLanguage):
    translatorDeepL = TranslatorDeepL(apiKeyDeepL)
    try:
        translation = translatorDeepL.translate(text, target_lang=destinationLanguage)
    except:
        translation = ""
        print("Probably unsupported language symbol. No translation possible")
    return translation.text