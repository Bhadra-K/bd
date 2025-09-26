import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
data=pd.read_csv("iris.csv")
print(data.head())
print(data['Species'].value_counts)

x=data[['Id','Sepal Length (cm)','Sepal Width (cm)','Petal Length (cm)','Petal Width (cm)']]
y=data['Species']


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print(f"Accuracy: ",accuracy_score(y_pred,y_test))
print(f"Classification Report: ",classification_report(y_pred,y_test))
print(f"Confusion Matrix: ",confusion_matrix(y_pred,y_test))