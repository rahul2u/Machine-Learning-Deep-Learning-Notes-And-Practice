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

'''
you have learned about the shorthand character 
classes and also how to declare your own custom anonymous character 
class using the square bracket ("[]" ) symbol. Now, the reason I wanted 
to add this article is to let you know that we have made one mistake 
while declaring the anonymous character class.

In our example, we have used the character class "[@%#~+-\.\']"   . This 
works but it has a problem. The problem is with the "-"  character. The "-"  
character in regex has a special meaning. It means a range of characters. 
So, in our example, "+-\."  means the range of characters from "+"  to "."  in terms
of their ASCII value (the range from 43-46), not the three characters themselves.
In our case this mistake doesn't result in an error and still works as the range 
43-46 is a valid range. But, by mistake if you put here something like "+-#"  then
it would result into an error as the ASCII range would 43-35 which is invalid.

Therefore, the best thing to do whenever you want to just track "-"  is to escape it, i.e. "\-" .

'''
