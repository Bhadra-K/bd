import pandas as pd
#Series - 1D labeled aray
s=pd.Series([10,20,30,40])
print(s)
#DataFrame 
data={'Name':['Alice','Bob','Jack'],'Age':[25,30,22]}
df=pd.DataFrame(data)
print(df)
#df.head
data={'Name':['Alice','Bob','Jack','Mary','Robert','Charles','Lucy'],'Age':[25,30,22,18,19,28,16]}
df=pd.DataFrame(data)
print(df.head())        #returns the 1st 5 rows by default if no argument
print(df.head(3))
#df.tail
print(df.tail())    #returns the last 5 rows
print(df.tail(2))
#df.info]
data={'Name':['Alice','Bob','Jack',None],'Age':[25,30,None,22],'Grade':['A','B','C','A']}
df=pd.DataFrame(data)
df.info()