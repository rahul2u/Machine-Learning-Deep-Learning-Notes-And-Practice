import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple is acquired a new U.K. based company in 1$ billion ."
doc = nlp(text)   # return a  doc type objects or Doc
print(doc)
print(type(doc))

# see the all tokens
for token in doc:
    print(type(token))  # <class 'spacy.tokens.token.Token'>
    print(token)
    print(type(token.text))
    print(token.text)  # <class 'str'>


# Doc object is iterable object
# part of speech
for token in doc:
    print(f'{token.text:{15}} {token.pos_}')
