import pandas as pd
import numpy as np
#Series - 1D labeled aray
s=pd.Series([10,20,30,40])
print(s)
# #DataFrame 
data={'Name':['Alice','Bob','Jack'],'Age':[25,30,22]}
df=pd.DataFrame(data)
print(df)
# #df.head
data={'Name':['Alice','Bob','Jack','Mary','Robert','Charles','Lucy'],'Age':[25,30,22,18,19,28,16]}
df=pd.DataFrame(data)
print(df.head())        #returns the 1st 5 rows by default if no argument
print(df.head(3))
# #df.tail
print(df.tail())    #returns the last 5 rows
print(df.tail(2))
# #df.info]
data={'Name':['Alice','Bob','Jack',None],'Age':[25,30,None,22],'Grade':['A','B','C','A']}
df=pd.DataFrame(data)
df.info()
# #df.describe
print(df.describe())
# #df.columns - returns labels
print(df.columns)
# #df.shape - tuple containing no of columns and rows 
print(df.shape)
#df.loc[]
data={'Name':['Alice','Bob','Jack'],'Age':[25,30,22],'City':['Delhi','Mumbai','Chennai']}
df=pd.DataFrame(data,index=['a','b','c'])
print(df.loc['a'])
print(df.loc['b','Name'])
print(df.loc[:,['Name','City']]) #all rows
#df.iloc[] - access row & cols by int position
print(df.iloc[0])   #1st row
print(df.iloc[1,0])  #2nd row 1st col
print(df.iloc[:,0:2])   #all rows, 1st 2 cols
#df.isnull
data={'Name':['Alice','Bob','Jack'],'Age':[25,np.nan,22],'City':['Delhi','Mumbai',None]}
df=pd.DataFrame(data)
print(df.isnull())
#df.dropna - null value row/col remove
print(df.dropna())
df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)
