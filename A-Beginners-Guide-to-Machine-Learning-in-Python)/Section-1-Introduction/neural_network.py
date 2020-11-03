from sklearn.neural_network import MLPClassifier
import pandas as pd

data = pd.read_csv("spambase/spambase.data")
X = data.drop(['1'], axis=1)
Y = pd.DataFrame(data, columns=['1'])
model = MLPClassifier()
model.fit(X,Y)
accuracy = model.score(X,Y)
print(accuracy)
# import pandas as pd
# from sklearn.neural_network import MLPClassifier
#
# Data = pd.read_csv("spambase/spambase.data")
#
# Data = Data.sample(frac=1)
#
# X = Data.drop(["1"],axis=1)
# Y = pd.DataFrame(Data,columns=["1"])
#
#
# MLP = MLPClassifier()
#
# MLP.fit(X,Y)
# Accuracy = MLP.score(X,Y)
#
# print(Accuracy)
#
#
#
#
