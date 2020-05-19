# Find and replace function in regular expression
# re.sub() find and replace function,that is global search function,that have 5 parameters

import re
sentence = "I love Avengers"
replace = re.sub(r"Avengers", "Justice league", sentence)
print(replace)
replace = re.sub(r"[a-zA-Z]","0",sentence)
print(replace)

replace = re.sub(r"[a-z]","0",sentence, flags= re.I)  # re.I case insensitive
print(replace)

replace = re.sub(r"[a-z]","0",sentence, 1 , flags= re.I)
print(replace)