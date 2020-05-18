import re
# re.match() = local search not global search
# re.match function use  searching the pattern
sentence = "I was born in 1990"
sentence2 = "1990 was the year of when I born"
match = re.match(r"[a-zA-Z]+", sentence2)
print(match)   # None return because match looks the First patterns not going to the whole sentence
# it looks the first pattern in whole sentence .Its not going to to look in at whole sentence.





