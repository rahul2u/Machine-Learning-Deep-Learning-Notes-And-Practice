import numpy as np

arr = np.arange(1, 10)
print(arr)
arr = np.arange(10, dtype= 'float64')
print(arr)

# Examine numpy array
arr = np.arange(1, 10)
print(arr.size)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.itemsize)
print("Memory:",arr.itemsize * arr.size)

# convert list to array
list = [1, 2, 3, 4, 5, 6]
arr = np.asarray(list)
print(type(arr))
list = [[1, 2, 3, 4], [4, 5, 6, 7]]
print(list)


# linspace
arr = np.linspace(1, 4 , num= 10)
print(arr)
arr = np.linspace(1,4, num= 10, endpoint= False)
print(arr)

# np.random.random()
arr = np.random.random((3 , 4) )
print(arr)

print(np.max(arr))  # find max whole matrix
print(np.max(arr, axis= 1)) # max in row by row
print(np.max(arr, axis= 0)) # max column by column


print(np.min(arr))  # find min whole matrix
print(np.min(arr, axis= 1)) # min in row by row
print(np.min(arr, axis= 0)) # min column by column


print(np.median(arr))  # find max whole matrix
print(np.median(arr, axis= 1)) # max in row by row
print(np.median(arr, axis= 0)) # max column by column

# reshape function
arr = np.reshape(arr,(12,))
print(arr)
arr = np.reshape(arr,(12,1))
print(arr)


# slicing
arr = np.random.random((4, 5))
print(arr[::])
print(arr[1:5, :])
print(arr[:, 1:3])
print(arr[1:3, 1:3])
print(arr[[1,3],:])
print(arr[:,[0,3]])
print(arr[:-1,:])
print(arr[-1:,:])
# The End





