import numpy as np
#zero ands ones array
a=np.array([1,2,3])
print(a)
print(np.zeros((2,3)))
print(np.ones((2,2)))
#range 
a=np.arange(0,10,2)
print(a)
#reshape
a=np.arange(6)
b=a.reshape((2,3))
print("Reshaped:",b)
#mean,median,standard deviation 
a=np.array([1,2,3,4,])
print(a)
print(np.mean(a))
print(np.median(a))
print(np.std(a))