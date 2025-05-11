import numpy as np

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

print(f"loaded {len(train_text)} train data points")
print(f"loaded {len(test_text)} test data points")
