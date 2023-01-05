from  sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
 
iris=datasets.load_iris()
x_iris=iris.data[:,2:4]
y_iris=iris.target
n_classess=3
for i in range (n_classess):
        index=np.where(y_iris==i)
        plt.scatter(x_iris[index,0],x_iris[index,1],label=iris.target_names[i])
        plt.legend()
        plt.xlabel(iris.feature_names[2])
        plt.ylabel(iris.feature_names[3])
plt.show()
 

 