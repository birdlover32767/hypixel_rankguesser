import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# data
def str_to_arr(text: str):
	if len(text) < 20:
		text = text + chr(0) * (20 - len(text))
	array = np.array([ord(i)-48 for i in text])
	return array

train_text = []; train_labels = []
test_text = []; test_labels = []
with open("training.txt") as f:
	for line in f.readlines():
		line = line[0:-1]
		train_labels.append(int(line[0]))
		train_text.append(str_to_arr(line[1:-1]))
with open("testing.txt") as f:
	for line in f.readlines():
		line = line[0:-1]
		test_labels.append(int(line[0]))
		test_text.append(str_to_arr(line[1:-1]))
train_text = np.array(train_text); train_labels = np.array(train_labels)
test_text = np.array(test_text); test_labels = np.array(test_labels)

class_names = ["None", "VIP", "VIP+", "MVP", "MVP+", "MVP++"]

# the model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(20,)),
    tf.keras.layers.Dense(128, activation="leaky_relu"),
	tf.keras.layers.Dense(112, activation="leaky_relu"),
    tf.keras.layers.Dense(6)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_text, train_labels, epochs=20)

test_loss, test_acc = model.evaluate(test_text, test_labels)
print("\nAccuracy:", test_acc)

# probability
#probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
#predictions = probability_model.predict(np.array([str_to_arr("+++++")])) # replace the np.array...whatever with test_text for their probabilities
#print(predictions)