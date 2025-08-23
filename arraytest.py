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
#random float no in range[0,1]
x=np.random.rand()
print(x)
y=np.random.rand(5)
print(y)
z=np.random.rand(2,3)
print(z)
#random integer
p=np.random.randint(1,10)
print(p)
q=np.random.randint(0,100,size=5)
print(q)
z=np.random.randint(10,21,size=(3,3))
print(z)

# generate 6-digit otp example
otp=np.random.randint(000000,1000000)
print(otp)
