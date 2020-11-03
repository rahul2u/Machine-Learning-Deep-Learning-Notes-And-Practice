# import Libraries
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# load data and splitting
data = pd.read_csv("spambase/spambase.data")
data = data.sample(data, frac=1)

x = data.drop(['1'], axis=1)
y = pd.DataFrame(data, columns=['1'])
# prepare and fit the model
model = KNeighborsClassifier()
model.fit(x, y)
prediction =model.score(x,y)
print(prediction)

#