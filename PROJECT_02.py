#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
from tensorflow import keras as ks
import numpy as np
import pandas as pd


# In[4]:


(train_images, train_labels), (test_images, test_labels) = ks.datasets.fashion_mnist.load_data()


# In[5]:


X_train = train_images.reshape(train_images.shape[0], 28, 28, 1)
X_test = test_images.reshape(test_images.shape[0], 28, 28, 1)


# In[6]:


X_train = X_train.astype('float32')
X_test = X_test.astype('float32')


# In[7]:


Y_train = ks.utils.to_categorical(train_labels, 10)
Y_test = ks.utils.to_categorical(test_labels, 10)


# In[12]:


input_shape = (28, 28, 1)


# In[13]:


model = ks.Sequential()
model.add(ks.layers.Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=input_shape))
model.add(ks.layers.Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(ks.layers.MaxPooling2D(pool_size=(2,2)))
model.add(ks.layers.Dropout(0.25))
model.add(ks.layers.Flatten())
model.add(ks.layers.Dense(128, activation='relu'))
model.add(ks.layers.Dropout(0.5))
model.add(ks.layers.Dense(10, activation='softmax'))
model.summary()


# In[14]:


model.compile(loss=ks.losses.categorical_crossentropy, optimizer='adam', metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=128, epochs=3, verbose=1, validation_data=(X_test, Y_test))


# In[15]:


score=model.evaluate(X_test, Y_test, verbose=0)
score


# In[ ]:




