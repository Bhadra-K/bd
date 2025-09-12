#HOUSE PRICE PREDICTION
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#x=House area y=House price
x=np.array([2500,2000,500,1500,3000]).reshape(-1,1)
y=np.array([12000,15000,130000,24357,23896])
model=LinearRegression()
model.fit(x,y)
print("Intercept(Base Price):",model.intercept_)
print("Slope(Price per sq.ft):",model.coef_[0])
size=1100
predicted_price=model.predict([[size]])
print(f"Predicted Price for {size} sq.ft: ${predicted_price[0]:2f}")
