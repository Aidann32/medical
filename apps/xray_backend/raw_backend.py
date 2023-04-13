#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
import pydicom as dicom 
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image


# In[3]:


train_dir='train'
val_dir='val'
test_dir='test'


# In[4]:


img_height=128
img_width=128
batch_size=32


# In[53]:


train_ds=tf.keras.preprocessing.image_dataset_from_directory(
 train_dir,
 color_mode='grayscale',
 image_size=(img_height,img_width),
 batch_size=batch_size
)

val_ds=tf.keras.preprocessing.image_dataset_from_directory(
 val_dir,
 color_mode='grayscale',
 image_size=(img_height,img_width),
 batch_size=batch_size
)

test_ds=tf.keras.preprocessing.image_dataset_from_directory(
 test_dir,
 color_mode='grayscale',
 image_size=(img_height,img_width),
 batch_size=batch_size
)


# In[54]:


train_ds.class_names


# In[55]:


plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.imshow(np.squeeze(images[i].numpy().astype("uint8")))
        plt.title(train_ds.class_names[labels[i]])
        plt.axis("off")


# In[8]:


AUTOTUNE=tf.data.experimental.AUTOTUNE
train_ds=train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds=train_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds=train_ds.cache().prefetch(buffer_size=AUTOTUNE)


# In[9]:


model = tf.keras.Sequential([
    layers.experimental.preprocessing.Rescaling(1./255),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(2, activation='softmax')
])


# In[10]:


model.compile(
optimizer='adam',
loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
metrics=['accuracy'])


# In[11]:


epochs=10


# In[12]:


model.fit(
train_ds,
validation_data=val_ds,
epochs=epochs)


# In[27]:


model.evaluate(test_ds)


# In[79]:


for images, labels in test_ds.take(1):
    for i in range(1):
        y = train_ds.class_names[labels[i]]
        img = np.squeeze(images[i].numpy().astype("uint8"))
y


# In[80]:


plt.imshow(img,cmap=plt.cm.gray)
plt.show()


# In[81]:


img.shape


# In[82]:


x = np.expand_dims(img, axis=0)
x = tf.keras.applications.xception.preprocess_input(x)


# In[83]:


preds = model.predict(x)


# In[84]:


preds_prob = np.max(preds)
preds_ind = np.argmax(preds)


# In[85]:


print("Вероятность ", preds_prob)
if preds_ind==0:
    print('Normal')
else:
    print('Pneumonia')


# In[ ]:




