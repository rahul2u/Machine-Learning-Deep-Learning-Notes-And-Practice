import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple is acquired a new U.K. based company in 1$ billion ."
doc = nlp(text)   # return a  doc type objects or Doc
print(doc)
print(type(doc))

# see the all tokens
for token in doc:
    print(type(token))  # spacy token calss
    print(token)
    print(type(token.text))
    print(token.text)