# list is non homogeneous data type
list =[1,2,3,4,'hello','world']
print(list)

# insert the element
#insert - insert in specific index
#apped - append function append element in last

list.insert(0,'good')
print(list)
list.append('india')
print(list)
list.insert(1,'bad things')
print(list)

# delete element in list

# pop -fuction delete last element
# del opratore delete index based  elements
# remove -function take one argument list index

list.pop()
print(list)
list.remove(list[1])
print(list)
del list[0]
print(list)

# updating the elements
list[0] ='very good'
print(list)

# looping lsit values
print("=====================================")
for index in range(0,len(list)):
    print(list[index],end =' ')
print()

for index in list:
    print(index,end =' ')
print()
print("***************************")
for index in range(len(list)):
    print(list[index],end=' ')
print()

i =0
length = len(list)
while i < length:
    print(list[i],end =' ')
    i +=1
print('***********************************8')
for i in list:
    print(i,end=' ')
