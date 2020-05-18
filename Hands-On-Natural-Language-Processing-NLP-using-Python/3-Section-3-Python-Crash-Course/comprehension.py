# list comprehension
# list comprehension is short form of loop

# Iterating list using loop
list1 =[1,2,3,4,5,6,7,8,9,10]
list2 = []
for number in list1:
    list2.append(number)
print(list2)

# You can do same thins using list comprehension

list2 = [number for number in list1]
print(list2)

list2 = [number for number in list1 if number >= 5]
print(list2)

list2 = [number for number in list1 if number%2 == 1]
print(list2)


# Generator comprehension
numbers =[1,3,5,9]
squarGen = (number ** 2 for number in numbers)
print(type(squarGen))
print(list(squarGen))


# Dictionary Comprehension
myDict ={'apple':1, 'banana':4, 'orange':3}
print(myDict)

newDict = {i for i in myDict}
print(newDict)

newDict = {i for i in myDict.keys()}
print(newDict)

newDict = {i for i in myDict.values()}
print(newDict)

newDict = {i for i in myDict.items()}
print(newDict)


newDict ={key:myDict[key] for key in myDict.keys()}
print(newDict)

newDict = {key:myDict[key] for key in myDict.keys() if myDict[key] >3}
print(newDict)


# Join function list words in paragraph

myList =['I ','Love ','Adventure']
mySentence = ' '.join(myList)
print(mySentence)

mySentence = '*'.join(myList)
print(mySentence)