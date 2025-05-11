import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from data import *

class_names = ["None", "VIP", "VIP+", "MVP", "MVP+", "MVP++"]

# the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(112, activation="leaky_relu"),
    tf.keras.layers.Dense(6)
])
model.compile(optimizer="adam",
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=["accuracy"])
model.fit(train_text, train_labels, epochs=25)

test_loss, test_acc = model.evaluate(test_text, test_labels)
print("\nAccuracy:", test_acc)

# probability
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(np.array([str_to_arr("♥")])) # replace the np.array...whatever with test_text for their probabilities
print(predictions)