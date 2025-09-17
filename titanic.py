import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import seaborn as sns
#load dataset
data=sns.load_dataset("titanic")
print(data)
#check missing values
print(data.isnull().sum())
#split and keep only selected features and target
x=['pclass','sex','age','sibsp','parch','fare','embarked','who']
y=['survived']
data=data[x+y]
#handle missing values
data['age']=data['age'].fillna(data['age'].median())
data['embarked']=data['embarked'].fillna(data['embarked'].mode()[0])
#encoding
for col in ['sex','embarked','who']:
    data[col]=LabelEncoder().fit_transform(data[col])
#split train and test sets
x_train,x_test,y_train,y_test=train_test_split(data[x],data[y],test_size=0.5,random_state=42)
#model
model=LogisticRegression()
model.fit(x_train,y_train)
#predict on test data
y_pred=model.predict(x_test)
#evaluation
print(f"Accuracy:{accuracy_score(y_test,y_pred)}")
print("Classification Report:")
print(classification_report(y_test,y_pred))
print("Confusion matrix:")
print(confusion_matrix(y_test,y_pred))
