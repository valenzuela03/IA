import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

class EmotionModel:
    # constructor
    def __init__(self, data_dir, labels, model_path="modelo_emociones.h5"):
        self.data_dir = data_dir
        self.labels = labels
        self.model_path = model_path
        self.model = None

    # Se crea el modelo secuencial
    # Se utilizan capas convolucionales de activacion ReLU, capas de pooling maximo, y capas densas
    def build_model(self):
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
            MaxPooling2D(2, 2),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D(2, 2),
            Flatten(),
            Dense(128, activation='relu'),
            Dropout(0.5),
            Dense(len(self.labels), activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        self.model = model

    # se entrena el modelo en 10 epocas con un generador de imagenes
    def train(self, epochs=10, batch_size=32):
        datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
        train_gen = datagen.flow_from_directory(
            self.data_dir,
            target_size=(48, 48),
            color_mode='grayscale',
            batch_size=batch_size,
            class_mode='categorical',
            subset='training'
        )
        val_gen = datagen.flow_from_directory(
            self.data_dir,
            target_size=(48, 48),
            color_mode='grayscale',
            batch_size=batch_size,
            class_mode='categorical',
            subset='validation'
        )

        self.model.fit(train_gen, validation_data=val_gen, epochs=epochs)
        self.model.save(self.model_path)
        print(f"Modelo guardado en: {self.model_path}")
