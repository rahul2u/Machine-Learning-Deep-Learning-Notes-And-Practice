import re

sentence = "I am born in 1990"
re.match(r".*", sentence)
# r for regular expression, . mean any characters (a ..z ,0 to 1, ora ny Ascii characters(# ,@ symbol etc)
# * means zero and more
# and .* means  matches sequence of  any  ASCII characters length zero or more
re.match(r".+", sentence)
# .+ means  matches sequence of  any  ASCII characters length one or more(not Zero)
# sentence = ""
re.match(r".+", sentence)   # output  zero  pattern match
# match only character
match = re.match(r"[a-zA-Z]+", sentence)
print(match)

sentence = "abb"
match = re.match(r"ab?", sentence)  # after a zero or one b (more b not check)
print(match)

