import pandas as pd
import statistics as st
import numpy as np


df = pd.read_csv("Mall_Customers.csv")
print(df.mean())
print(df.median())
print(st.mode(df['Genre']))
print(np.mean(df['Age']))
