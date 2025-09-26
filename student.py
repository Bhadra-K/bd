import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.preprocessing import OneHotEncoder

data=pd.read_csv("student_performance_dataset.csv")
print(data.head())

print(data.isnull().sum())
data['Gender']=data['Gender'].map({'Male':0,'Female':1})
data['Internet_Access_at_Home']=data['Internet_Access_at_Home'].map({'No':0,'Yes':1})
data['Extracurricular_Activities']=data['Extracurricular_Activities'].map({'No':0,'Yes':1})
data['Pass_Fail']=data['Pass_Fail'].map({'Pass':1,'Fail':0})
print(data.head())
print(data.isnull().sum())

x=data[['Gender','Attendance_Rate','Study_Hours_per_Week','Past_Exam_Scores','Internet_Access_at_Home','Extracurricular_Activities','Final_Exam_Score']]
y=data['Pass_Fail']
# df=pd.DataFrame(data)
# onehot=pd.get_dummies(df['Student_ID'],dtype=int)
# data=data.drop('Student_ID',axis=1)
# data=data.join(onehot)
# print(data.head())

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print(f"Accuracy: ",accuracy_score(y_pred,y_test)*100,'%')
print(f"Classification Report: ",classification_report(y_pred,y_test))
print(f"Confusion Matrix: ",confusion_matrix(y_pred,y_test))