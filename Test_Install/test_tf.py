# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
print(tf.__version__)


# Helper libraries
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # Backend needed for the Mac virtual env
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
x = np.linspace(0,1,100)
plt.plot(x,np.sin(4*np.pi*x))
plt.show(block=False)
plt.pause(2)
plt.close()


# Test training
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(10, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)

print("\n\nScript was run successfully!!")





