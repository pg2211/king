
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
  
# Importing the dataset
datas = pd.read_csv('USA_Housing.csv')

X = datas.iloc[:, 1:2].values
y = datas.iloc[:, 2].values

from sklearn.linear_model import LinearRegression
lin = LinearRegression()
  
lin.fit(X, y)


# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
  
poly = PolynomialFeatures(degree = 4)
X_poly = poly.fit_transform(X)
  
poly.fit(X_poly, y)
lin2 = LinearRegression()
lin2.fit(X_poly, y)

plt.scatter(X, y, color = 'blue')
plt.show()

# Predicting a new result with Linear Regression after converting predict variable to 2D array
pred = 110.0
predarray = np.array([[pred]])
lin.predict(predarray)