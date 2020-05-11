import numpy as np
# 1 D array

a = np.array([1,2,3,4])
print(a)

# print dimensions
print(a.ndim)

# print shape
print(a.shape)

# length of array
print(len(a))

# 2D and 3 D array or 3D array

b = np.array([[1,2,3,4],[5,6,7,8]])
print(b)
print(b.ndim)
print(b.shape)
print(len(b))  # return the size of first dimentions


# 3 Dimentional list

c= np.array([[ [1,2], [4,5] ], [ [7,8], [10,11]]])
print(c)
print(c.ndim)
print(c.shape)            # tells us number of row and columns
print(len(c))            # lenght function tells us number of row



# using the arange function

d = np.arange(10)
print(d)

d = np.arange(1,100,2)  # start, end ,steps
print(d)


# using the linspace

e = np.linspace(0,1,6)  # start,end ,no of points that divide range 0,1 in six point
print(e)

# array of one

one = np.ones((3,3))
print(one)

# array of zeros

zero = np.zeros((3,4))
print(zero)

# Identity matrix

i = np.eye((3))   #2d array
print(i)

i = np.eye(2,3)   # 2 row and 3 column  diagonal vector
print(i)

# create a diagonal function

d = np.diag([1,2,3,4])
print(d)

# extract diagonal
print(np.diag(d))

# Random number genration

r = np.random.rand(4)                      # uniform normal distribution number (0 to 1 value have equal probability)
print(r)

r = np.random.randn(4) # standard normal distribution
print(r)


# data types of numpy
#  default data type arange function is intiger types
a = np.arange(10,dtype = 'float64')
print(a)
print(a.dtype)

# zeros and ones function default data type is float64

# complex array

c = np.array([3+4j,5+6j])
print(c)

# staring array
s = np.array(['Ram','Sita','Lakshman'])
print(s)
print(s.dtype)

# array of Boolen
b = np.array([True,False,True,False])
print(b)
print(b.dtype)


# access element and assignment of element

c =  np.diag([1,2,3])
print(c)
print(c[2,2])

# assigning value
c[2,2] = 14
print(c)


# slicing and assignment

a = np.arange(20)
print(a[0:20:2])
# asignment
a[5:] = 10
print(a)

b = np.arange(15)
a[5:]=b[::-1]
print(a)


# view and copy

a = np.arange(20)
b = a[0::2]
print("final-------")
print(a)
print(b)
print(np.shares_memory(a,b))

b = a[0::2].copy()
print(np.shares_memory(a,b))


# important funtions
#np.arange()
#np.array()
#np.random.rand()
#np.random.randn()
#np.random.randint()

#masks is boolen (it is copy not view)

a = np.random.randint(0,20,15)
print(a)
mask =(a % 2 == 0)
extract_from_a = a[mask]
print(extract_from_a)

# assigning value in mask

a[mask] = -1
print(a)

# indices as array
print(a[[2,3,3,3]])

# assined of new values
a[[9,4]]=-200
print(a)
