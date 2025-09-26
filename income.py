import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
data=pd.read_csv("adult.csv")
print(data.head())  
print(data.isnull().sum())
x=data[['age','fnlwgt','education.num','capital.gain','capital.loss','hours.per.week']]
y=data[[]]