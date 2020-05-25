import pandas as pd
import numpy as np

mySeries = pd.Series([1,2,3,4,5,6])
print(mySeries)
larger_than_2 = mySeries > 2
mySeries = mySeries + 2000
print(mySeries)


print(larger_than_2)
print("=====================================")
print(larger_than_2.any())
print(larger_than_2.all())


# apply function
def square(x):
    return  x**2

print(mySeries.apply(square))

# convert data type

mySeries = mySeries.astype(np.float64)
print(mySeries)

# copy

y = mySeries
y[0] = 20
print(y[0])
print(mySeries[0])  # that is reference not copying

y = mySeries.copy()
y[0] = 12
print(y[0])
print(mySeries[0])

# Series - 1D or single column
# DataFrame - multiple column

data =[1,2,3,4,5,6,7]
df = pd.DataFrame(data,columns= ['x'])
print(df)

# adding columns
df["x_squre"] = df["x"].apply(np.math.sqrt,)
print(df)
df["x_factorial"] =df["x"].apply(np.math.factorial)
print(df)
df["x_plus"] = df["x"] + 2
print(df)

# dropping/deleting columns
# df = df.drop("x_square")
print(df)

# selecting multiple columns
#print(df['x_squre', 'x_factorial'])


# # describe
print(df.describe())

# read data
#csv_to_dataframe = pd.read_csv("")





