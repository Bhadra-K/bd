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

#5. build a simple CNN model
model=models.Sequential([           #sequential is a container that stores layers
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),  #convolution      (#activation signals=relu,leaky relu,sigmoid,tanh,softmax)
    layers.MaxPooling2D((2,2)),  #pooling layer         #max pooling,average pooling
    layers.Flatten(),    #flatten into 1D                                   (#dense layers does not process 2d)
    layers.Dense(64,activation='relu'), #fully connected layer              (#relu gives 0 output for 0/-ve no. and same number for +ve no.)
    layers.Dense(10,activation='softmax') #output layer (10 classes)        (#use softmax when there r diff/multi-classes)
])  #eg: A basket with pictures of fruits.Look closely (Conv2D + ReLU) → zoom out (MaxPooling) → line up features (Flatten) → helpers analyze features (Dense+ReLU) → pick fruit with highest chance (Dense+Softmax)

#6. compile model
model.compile(optimizer='adam',     #SGD,Adam,RMSprop       optimizer-adjusts weights(correction of faults)
              loss='sparse_categorical_crossentropy',       #loss fun-measure how wrong the prediction is compared to real ans.
              metrics=['accuracy'])

#7. train the model
history=model.fit(x_train,y_train,
                  epochs=5,     #how many times the value needs to pass through network. if bigger value then time increases but accuracy also increases.
                  batch_size=64,    #faster training
                  validation_data=(x_test,y_test),
                  verbose=1)    #shows progress bar     #after each epochs the result needs to be shown then give 1 or 0 for no visibility 

#8. evaluate on test data
test_loss,test_acc=model.evaluate(x_test,y_test,verbose=0)
print("Test Accuracy:",round(test_acc*100,2),"%")

#9. predict example
prediction=model.predict(x_test[:1])    #get prediction probabilities
predicted_label=prediction.argmax()     #find the most likely class

plt.imshow(x_test[0].reshape(28,28),cmap="gray")
plt.title("Prediction: " +str(predicted_label))
plt.axis("off")
plt.show()

# steps
# 1.input image and preprocess/normalize    -scale pixel values to 0-1
# 2.convolutional layer -extract features using filters
# 3.activation fun  -apply relu to add nonlinearity
# 4.pooling layer
# 5.flattening layer
# 6.dense(fully connected)layer -analyze features and learn patterns
# 7.output layer    -use softmax for multi-class classification