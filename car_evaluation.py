import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.metrics import classification_report
#load dataset
columns=['buying','maint','doors','persons','lug_boot','safety','class']
data=pd.read_csv("C:car.data",names=columns)
print(data)
print(data.isnull().sum()) #preprocessing
#features and target
x=data[['buying','maint','doors','persons','lug_boot','safety']]
y=data['class']
#encode target-class using LabelEncoder
le_target = LabelEncoder()
y_encoded = le_target.fit_transform(y)
#split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=42)
#use OneHotEncoder on all columns
preprocessor=ColumnTransformer(transformers=[("col_enc",OneHotEncoder(handle_unknown='ignore'),x.columns)])
x_train_encoded=preprocessor.fit_transform(x_train) 
x_test_encoded=preprocessor.transform(x_test)
#model
model=LogisticRegression()
model.fit(x_train_encoded,y_train)
#evaluation 
print("Training accuracy:",model.score(x_train_encoded,y_train))
print("Test accuracy:",model.score(x_test_encoded,y_test))
#predict on test data
y_pred_encoded = model.predict(x_test_encoded)
#classification report with original class names
print("\nClassification Report:")
print(classification_report(y_test, y_pred_encoded, target_names=le_target.classes_))