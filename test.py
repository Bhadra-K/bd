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
#pltbar()=vertical bar plot
categories=['A','B','C']
values=[3,7,5]
plt.bar(categories,values,color=['red','green','blue'])
plt.title("Bar plot")
plt.show()
#plt.barh()=horizontal bar plot
categories=['A','B','C']
values=[3,7,5]
plt.barh(categories,values,color=['yellow','orange','brown'])
plt.title("Horizontal Bar plot")
plt.show()
#plt.hist()=histogram
data=np.random.randn(1000)
plt.hist(data,bins=30,color='skyblue',edgecolor='black')
plt.title("Histogram")
plt.show()
#plt.pie()=pie chart
sizes=[20,30,40,25]
labels=['A','B','C','D']
plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)
plt.title("Pie Chart")
plt.show()
#Advanced plotting functions
#plt.stackplot()=stacked area plot
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,5,7]
working=[9,4,5,7,2]
playing=[2,2,4,6,12]
plt.stackplot(days,sleeping,eating,working,playing, labels=['Sleep','Eat','Work','Play'])
plt.legend(loc='upper left')
plt.title("Stacked area plot")
plt.show()
#plt.boxplot()=Box plot
data=np.random.normal(100,20,200)
plt.boxplot(data)
plt.title("Box plot")
plt.show()
#sns.histplot()=Histogram+KDE
import seaborn as sns
df=sns.load_dataset("tips") #restaurant tips dataset
sns.histplot(df["total_bill"],bins=20,kde=True,color="yellow")
plt.title("Histogram + KDE")  #KDE=yellow line (show data flow) [Kernel Density Estimation plot]
plt.show()
#sns.barplot()=Bar plot(with error bars)
data=pd.DataFrame({
    "category":['A','B','C','D'],
    "value":[4,7,2,9]
})
sns.barplot(x="category",y="value",data=data)
plt.title("Normal Bar Chart (Seaborn)")
plt.show()
#sns.countplot()=Count of categories
sns.countplot(x="day",data=df,palette="Set2")
plt.title("Count plot")
plt.show()
#sns.boxplot()=Box plot
sns.boxplot(x="day",y="total_bill",data=df,palette="pastel")
plt.title("Box plot")
plt.show()
#sns.scatterplot()=Scatter plot
sns.scatterplot(x="total_bill",y="tip",data=df,hue="sex",style="time")
plt.title("Scatter plot")
plt.show()