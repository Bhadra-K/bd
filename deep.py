#CNNIMAGEPROCESSING
#1. import libraries
import tensorflow as tf
from tensorflow.keras import layers,models
import matplotlib.pyplot as plt
#2. load dataset(MNIST is a built in data)
(x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data()
print((x_train,y_train),(x_test,y_test))
#3. normalize data(scale pixel values to 0-1)
x_train=x_train.astype("float32") / 255.0
x_test=x_test.astype("float32") / 255.0
#4. reshape data(CNN expects 3D: height,width,channels)
x_train=x_train.reshape(-1,28,28,1)     #-1 means "figure this dimension out automatically"
x_test=x_test.reshape(-1,28,28,1)       #1 is the no of channels
