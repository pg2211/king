
import matplotlib.pyplot as plt

x=[2010,2012,2014,2016,2018,2020]
y=[45,55,60,57,45,42]

plt.scatter(x,y,color="green",label="lakh")
plt.legend()
plt.title("scatter plot")
plt.xlabel("year")
plt.ylabel("Profit")
plt.show()
