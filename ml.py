import pandas as pd
from sklearn.datasets import load_breast_cancer #labelled dataset    (or use kaggle for datasets)
from sklearn.model_selection import train_test_split #train and test
from sklearn.linear_model import LogisticRegression #algorithm
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix #validation
import seaborn as sns
import matplotlib.pyplot as plt  #seaborn and matplotlib-visualisation tools


#--------------DATA-------------------
data=load_breast_cancer()
df=pd.DataFrame(data.data,columns=data.feature_names)
df["target"]=data.target   #0-malignant  1-benign
#keep only 5 imp features+target
df_small=df[["mean radius","mean texture","mean perimeter","mean area","mean smoothness","target"]] #target=result column
#2.Split dataset
x=df_small.drop(columns=["target"]) #q part
y=df_small["target"] #result part
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y) #testsize-only 20% is tested.  randomstate-every time show same data while load.   stratify-grping based on result-clustering technnique


#-------------MODEL CREATION----------------
#3.Train Logistic Regression
model=LogisticRegression()
model.fit(x_train,y_train)
#4.EValuation
y_pred=model.predict(x_test)
y_prob=model.predict_proba(x_test)[:,1]
print("Model Accuracy:",accuracy_score(y_test,y_pred))
print("\nClassification Report:\n",classification_report(y_test,y_pred))

#-----------------EVALUATION-----------
#Confusion Matrix 
cm=confusion_matrix(y_test,y_pred) #gives a matrix fig. if actual data=benign and predicted also benign then true.likewise both malignant then true. if actual=benign and predicted=malignant then false. 
plt.figure(figsize=(5,4))
sns.heatmap(cm,cmap="Blues",
            xticklabels=["Malignant","Benign"], yticklabels=["Malignant","Benign"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


#------------------PREDICTION---------------------
# 5. User Input Prediction
print("\n--- Breast Cancer Prediction ---")
mean_radius = float(input("Enter mean radius (e.g. 14.5): "))
mean_texture = float(input("Enter mean texture (e.g. 20.0): "))
mean_perimeter = float(input("Enter mean perimeter (e.g. 100.0): "))
mean_area = float(input("Enter mean area (e.g. 900.0): "))
mean_smoothness = float(input("Enter mean smoothness (e.g. 0.1): "))
# Create DataFrame for user input
user_data = {
    "mean radius": mean_radius,
    "mean texture": mean_texture,
    "mean perimeter": mean_perimeter,
    "mean area": mean_area,
    "mean smoothness": mean_smoothness
}
user_df = pd.DataFrame([user_data])
# Predict
prediction = model.predict(user_df)[0]
if prediction == 1:
    print(f"\n Prediction: Benign (Not Cancerous) ")
else:
    print(f"\nPrediction: Malignant (Cancerous) ")