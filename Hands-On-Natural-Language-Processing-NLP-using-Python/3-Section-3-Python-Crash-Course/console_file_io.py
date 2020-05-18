# Console input

statment1 = input("Enter your name:")
statment2 = int(input("Enter your Age:"))
print(statment1)
print(statment2)

# file I/O
data_write_file = input("Enter the data to write a file")
with open('data.txt','w') as f:
    f.write(data_write_file +'\n')


with open("data.txt",'a') as f:
    f.write(data_write_file +'\n')


with open("data.txt",'r') as f:
    print(f.read())

