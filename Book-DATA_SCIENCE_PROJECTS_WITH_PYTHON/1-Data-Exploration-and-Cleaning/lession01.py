# import pandas as pd
import numpy as np
import matplotlib as mlp

# random function
for i in range(1, 6):
    print(i)

# create a list using range function
my_list = list(range(1,8))
print(my_list)
print(type(range(8)))
a= range(8)
print(a)

# dictionary
my_dict = {}

# for loop
for i in range(5):
    print(i)

for i in my_list:
    print(i)

my_dict["oranges"] = 12
my_dict["banana" ] = 23

#print(my_dict)
new_list = sorted(list(my_dict.keys()) + ["pear"])
print(sorted(new_list))
#print(list(my_dict.values()))

class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value

    # Main Function


dict_obj = my_dictionary()

dict_obj.add(1, 'Geeks')
dict_obj.add(2, 'forGeeks')

print(dict_obj)