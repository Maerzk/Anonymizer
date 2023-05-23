from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Nick and I live in Berlin"

def anonymize(sentence):
    ner_results = nlp(sentence)
    print(ner_results)

    for i in ner_results:
        sentence = sentence.replace(i["word"], "[]")
    
    return sentence
