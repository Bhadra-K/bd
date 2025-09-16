import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
#load dataset
data=pd.read_csv("C:Mall_Customers.csv")
print(data)
#preprocessing
print(data.isnull().sum())
#encoding-labelencoder
data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})   #or   le = LabelEncoder()  (nextline)  data['Gender'] = le.fit_transform(data['Gender'])
print(data.head())
#access only annual income and spending score columns-index 3 & 4
x=data.iloc[:,[3,4]].values
print(x)
#clustering 
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42) #algorithm
    kmeans.fit(x)
    wcss.append(kmeans.inertia_) #max possible ways to generate best cluster 
#elbow graph
sns.set()
sns.lineplot(x=range(1,11),y=wcss,color="blue")
plt.title("The Elbow Point Graph")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.show()
#shows graph with bend in 5. So no of clusters=5
clusters=5
kmeans=KMeans(n_clusters=5,init='k-means++',random_state=0)
y=kmeans.fit_predict(x)
print(y)
clusters=0,1,2,3,4
plt.figure(figsize=(8,8))
plt.scatter(x[y==0,0],x[y==0,1],s=50,c="blue",label="cluster-1")
plt.scatter(x[y==1,0],x[y==1,1],s=50,c="green",label="cluster-2")
plt.scatter(x[y==2,0],x[y==2,1],s=50,c="pink",label="cluster-3")
plt.scatter(x[y==3,0],x[y==3,1],s=50,c="black",label="cluster-4")
plt.scatter(x[y==4,0],x[y==4,1],s=50,c="gray",label="cluster-5")
#centroids
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c="red",label="centroid")
plt.title("Customer Group")
plt.xlabel("Annual Income")
plt.show()

#steps
# import library
# preprocessing
# load algorithm
# elbow graph predict-no of clusters
# clusters from elbow graph given to alg
# plot graph