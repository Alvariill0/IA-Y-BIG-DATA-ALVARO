#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

print(f"versión de tensorflow: {tf.__version__}")

# cargar datos
xs=np.array([2,3,4,7,8,10],dtype=float)
ys=np.array([1,5,11,41,55,89],dtype=float)

# crear modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1)
])


#compilar el model
model.compile(optimizer='sgd',loss='mean_squared_error')

#visualizar modelo
model.summary()

#entrenar
model.fit(xs,ys,epochs=5)

#predecir
variable=model.predict(tf.constant([5]))
print(variable)

