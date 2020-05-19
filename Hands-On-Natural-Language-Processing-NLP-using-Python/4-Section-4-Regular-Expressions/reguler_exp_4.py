# shorthand character classes


import re

sentence1 = "Welcome to the year 2018"
sentence2 = "Just ~% ++++++ ==== arrived at @jack's place. #fun123"
sentence3 = "I                         love                  you"

sentence1_modified = re.sub(r"\d", "", sentence1)
print(sentence1_modified)
sentence2_modified = re.sub(r"[~%+#+@\.\'=]", "", sentence2)
print(sentence2_modified)
sentence2_modified = re.sub(r'\w', " ", sentence2) # show the different spam symbol you know the just ASCII characters
# not show any word characters or digit or the this in woke word character class (a-zA-Z1-0 find and replace space)
print(sentence2_modified)
# opposite
sentence2_modified = re.sub(r"\W", " ", sentence2) # W = Not word characters, w = word characters
print(sentence2_modified)


# removing the space
sentence2_modified = re.sub(r"\s+", " ", sentence2_modified)
print(sentence2_modified)

# removing the single character
sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+", " ", sentence2_modified)
print(sentence2_modified)

# remove space and replace
sentence3_modified = re.sub(r"\s+love\s+", " hate ", sentence3)
print(sentence3_modified)
