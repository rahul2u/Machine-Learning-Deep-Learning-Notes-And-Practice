import pandas as pd
import matplotlib as plt
from sklearn import (
        tree,
        ensemble,

)

url = (
"http://biostat.mc.vanderbilt.edu/"
"wiki/pub/Main/DataSets/titanic3.xls"
)

# Load data in dataframe

df = pd.read_excel(url)
orig_df = df
print(df.head())


