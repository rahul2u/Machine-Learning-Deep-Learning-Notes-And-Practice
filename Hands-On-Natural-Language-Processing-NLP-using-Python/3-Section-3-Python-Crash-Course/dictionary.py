dict1 ={}
dict1['fruita']="apple"
dict1['vegiatables']='tomato'
print(dict1)

for i in dict1.items():
    print(i[1])
    #print(dict1[i])


print(dict1.get("fruita"))
print(dict1.get("fruitaaa","Key is not exist"))
print(dict1.items())

# delete element in dictionary

#del dict1['fruita']
listOfKey = dict1.keys()
print(type(listOfKey))
listOfKey = list(dict1.keys())
print(type(listOfKey))
print(listOfKey)
listOfValues =list(dict1.values())
print(listOfValues)


# iterating the dictionary
for key in dict1.keys():
    print(dict1[key])

for value in dict1.values():
    print(value)

