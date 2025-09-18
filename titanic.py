# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Titanic dataset
data = pd.read_csv("train.csv")  
print(data.head())  #891 rows x 12 columns
# Check for missing values
print("Missing values before handling:")
print(data.isnull().sum())

# Fill missing values
data['Age'] = data['Age'].fillna(data['Age'].median())
print(data['Embarked'].mode())   #0 S
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

# Drop unnecessary columns
data = data.drop(columns=['Cabin', 'Ticket', 'Name'])

# Encode categorical variables
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Embarked'] = data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# Define features and target
x = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked']]
y = data['Survived']

# Split into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Model creation
model = LogisticRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

# Print results
print(f"Accuracy: {accuracy:.4f}\n")
print("Classification Report:")
print(report)
print("Confusion Matrix:")
print(matrix)

#plot
sns.set()
sns.countplot(x='Survived', data=data)
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()
