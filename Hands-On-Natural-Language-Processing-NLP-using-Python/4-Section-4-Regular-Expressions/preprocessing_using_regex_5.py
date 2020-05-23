import re

x = ["This is wolf #scary",
     "Welcome to jungle #missing",
     "12343 is number to know",
     "Remember the name s - Jhon",
     "I love      you"]

for i in range(len(x)):
    x[i] = re.sub(r"\W", " ", x[i])
    x[i] = re.sub(r"\d", " ", x[i])
    x[i] = re.sub(r"\s+[a-z]\s+", " ", x[i], flags=re.I)
    x[i] = re.sub(r"\s+", " ", x[i])
    x[i] = re.sub(r"^\s", "", x[i])
    x[i] = re.sub(r"\s$", "", x[i])
print(x)