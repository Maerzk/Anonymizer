from translate import *
from anonymize import *

text = '''El servicio al cliente fue excelente. Me atendieron de manera amable y resolvieron todas mis dudas. 
El producto superó mis expectativas en cuanto a calidad y funcionalidad. La entrega fue puntual y sin contratiempos. 
Estoy muy contento con mi compra y lo recomendaré a mis amigos. Si tiene alguna pregunta, puede ponerse en contacto conmigo. 
Mi nombre es Lucas García.'''

if __name__ == '__main__':
    # print("Input text to anonymize here:")
    # text = input()
    text = translateGoogle(text, "en")
    print(anonymize(text))