from googletrans import Translator as TranslatorGoogle
# from deepl import Translator as TranslatorDeepL

def translateGoogle(text, destinationLanguage):
    translatorGoogle = TranslatorGoogle()
    if destinationLanguage == "en": 
        translation = translatorGoogle.translate(text)
    else:
        translation = translatorGoogle.translate(text, dest=destinationLanguage)
    print(translation.text)

translateGoogle("El servicio al cliente fue excelente. Me atendieron de manera amable y resolvieron todas mis dudas. El producto superó mis expectativas en cuanto a calidad y funcionalidad. La entrega fue puntual y sin contratiempos. Estoy muy contento con mi compra y lo recomendaré a mis amigos.", "en")