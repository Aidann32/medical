#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
import pydicom as dicom 
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image


# In[2]:


train_dir='train'
val_dir='val'
test_dir='test'


# In[3]:


img_height=128
img_width=128
batch_size=32


# In[4]:


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


# In[5]:


train_ds.class_names


# In[6]:


plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.imshow(np.squeeze(images[i].numpy().astype("uint8")))
        plt.title(train_ds.class_names[labels[i]])
        plt.axis("off")


# In[7]:


AUTOTUNE=tf.data.experimental.AUTOTUNE
train_ds=train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds=train_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds=train_ds.cache().prefetch(buffer_size=AUTOTUNE)


# In[8]:


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


# In[9]:


model.compile(
optimizer='adam',
loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
metrics=['accuracy'])


# In[10]:


epochs=10


# In[11]:


model.fit(
train_ds,
validation_data=val_ds,
epochs=epochs)


# In[93]:


model.evaluate(test_ds)


# In[94]:


path  = 'pnevmoniya-4.jpg'


# In[95]:


from PIL import Image
img = Image.open(path).convert('L').resize((128, 128), Image.ANTIALIAS)
img = np.array(img)
img = img/255
img


# In[96]:


preds = model.predict(img[None,:,:])


# In[97]:


preds_prob = np.max(preds)
preds_ind = np.argmax(preds)


# In[98]:


print("Вероятность ",preds_prob)
if preds_ind==0:
    print('Normal')
else:
    print('Pneumonia')


# In[ ]:




