# #datset handling
# import pandas as pd
# data=pd.read_csv("C:MISSING_DATASET_HANDLING.csv",encoding='latin1')
# print(data.isnull().sum())
# #handle missing values- drop columns with too many missing values
# data=data.drop(columns=["ADDRESSLINE2"])
# print(data.isnull().sum())
# #drop rows with very few missing values
# data=data.dropna(subset=["ORDERDATE","PRODUCTLINE"])
# print(data.isnull().sum())
# #fill missing values(Imputation)-numeric columns(MSRP,YEAR_ID)-use mean/median
# #data["MSRP"]=data["MSRP"].fillna(data["MSRP"].median()) -using median (the median value will be filled in those missing places)
# data["POSTALCODE"]=data["POSTALCODE"].fillna(data["POSTALCODE"].mode()[0])#cant use median bcoz its string
# print(data.isnull().sum())
# #categorical columns(status,productline,custname)-use mode
# data["TERRITORY"].fillna(data["TERRITORY"].mode()[0],inplace=True)
# print(data.isnull().sum())
# #phone numbers or addresses
# data["PHONE"].fillna("Unknown",inplace=True) 
# print(data.isnull().sum())
#if dataset is large-use KKN Imputer/Iterative Imputer from sklearn to estimate missing values-advanced imputation
from sklearn.impute import KNNImputer
import pandas as pd
data=pd.read_csv("C:MISSING_DATASET_HANDLING.csv",encoding='latin1')
print(data.isnull().sum())
imputer= KNNImputer(n_neighbors=5)
data_imputed=pd.DataFrame(imputer.fit_transform(data.select_dtypes(include=[float,int])),
                          columns=data.select_dtypes(include=[float,int]).columns)
print(data_imputed.isnull().sum())