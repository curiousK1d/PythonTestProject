
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(1,21,2)
y = np.arange(20,0,-2)
y2= np.arange(1,21,2)

print("\n Values of X : \n " +str(x))
print("\n Values of Y : \n " +str(y))

# Line plot
plt.plot(x,y,color="red",linewidth=3)
plt.plot(x,y2,color="blue",linewidth=3)
plt.title("Line Plot")
plt.xlabel("X axis")
plt.ylabel("y Axis")

plt.show()

# Bar Plot
plt.bar(x,y)
plt.show()

# Scatter plot
startup = pd.read_csv("resources\\50_Startups.csv")
plt.scatter(startup["State"],startup["Administration"])
plt.show()

#Histogram
plt.hist(startup["Administration"])
plt.show()

#Boxplot

plt.show(startup.boxplot(column="R&D Spend",by="State"))
plt.show(startup.boxplot(column="Profit",by="State"))


#Seaborn
import seaborn as sb
plt.show(sb.boxplot(x=startup["State"],y=startup["Profit"]))
plt.show(sb.boxplot(startup["State"],startup["R&D Spend"]))