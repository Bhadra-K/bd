import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Basic plotting functions
# plt.plot=line plot
x=np.linspace(0,10,100)
y=np.sin(x)
plt.plot(x,y,color="green",linestyle="dotted",marker='*')   #linestyle=dotted,dashed,--,solid etc
plt.title("line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#plt.scatter()=scatter plot
x=np.random.rand(50)
y=np.random.rand(50)
plt.scatter(x,y,color="purple",marker="x")
plt.title("Scatter plot")
plt.show()
