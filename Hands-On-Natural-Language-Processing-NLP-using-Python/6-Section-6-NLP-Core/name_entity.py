import nltk

paragraph = "The Taj Mahal made by Emperor Shah Jahan"
words = nltk.word_tokenize(paragraph)
tagged_words = nltk.pos_tag(words)

name_entity = nltk.ne_chunk(tagged_words)
name_entity.draw()
print(name_entity)