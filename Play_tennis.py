import numpy as np
import pandas as pd

PlayTennis = pd.read_csv("PlayTennis.csv")

from sklearn.preprocessing import LabelEncoder
Le = LabelEncoder()

PlayTennis['outlook'] = Le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp'] = Le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity'] = Le.fit_transform(PlayTennis['humidity'])
PlayTennis['windy'] = Le.fit_transform(PlayTennis['windy'])
PlayTennis['play'] = Le.fit_transform(PlayTennis['play'])

y = PlayTennis['play']
X = PlayTennis.drop(['play'],axis=1)

# Fitting the model
from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, y)

# tree.plot_tree(clf)

print(tree.plot_tree(clf))

# # The predictions are stored in X_pred
# X_pred = clf.predict(X)

# # verifying if the model has predicted it all right.
# X_pred == y