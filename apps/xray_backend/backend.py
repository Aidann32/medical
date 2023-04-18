import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
import pydicom as dicom 
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image
from PIL import Image

import os


def predict_pneumonia_result(image_path):
    train_dir = os.path.join(os.getcwd(), 'apps', 'xray_backend', 'train')
    val_dir = os.path.join(os.getcwd(), 'apps', 'xray_backend','val')
    test_dir = os.path.join(os.getcwd(), 'apps', 'xray_backend','test')

    img_height=128
    img_width=128
    batch_size=32

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

    plt.figure(figsize=(10, 10))
    for images, labels in train_ds.take(1):
        for i in range(9):
            plt.subplot(3, 3, i + 1)
            plt.imshow(np.squeeze(images[i].numpy().astype("uint8")))
            plt.title(train_ds.class_names[labels[i]])
            plt.axis("off")

    AUTOTUNE=tf.data.experimental.AUTOTUNE
    train_ds=train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds=train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    test_ds=train_ds.cache().prefetch(buffer_size=AUTOTUNE)

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

    model.compile(
        optimizer='adam',
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])

    epochs = 10


    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs)
    
    model.evaluate(test_ds)

    path = image_path

    img = Image.open(path).convert('L').resize((128, 128), Image.ANTIALIAS)
    img = np.array(img)
    img = img/255
    print(img)


    preds = model.predict(img[None,:,:])

    preds_prob = np.max(preds)
    preds_ind = np.argmax(preds)

    # # 0 = Normal, 1 = Pneumonia
    return preds_ind 
