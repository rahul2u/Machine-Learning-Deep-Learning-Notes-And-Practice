# Regular expression or rejex  is a
# sequence  of characters that defines a specific search patterns
# and using which you can match or substitute patterns inside a text with least amount of code.

# pattern you are looking inside of text
# pattern can be year,email_id,mobile numbers,some one names etc.
# or
#  Regular Expression is tool or module  or  programing language that is use to find patterns  inside your text.


sentence = "I was born in the year 1996" # remove the text 1960

# using python first loop the string, then apply match and delete but regular expression you do it with in single line
import re
sentence = re.sub(r"\d", "", sentence)
print(sentence)









