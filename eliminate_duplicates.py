import copy

names = []
text = []
with open("training.txt", ) as f:
	for line in f.readlines():
		names.append(line[1:-1])
		text.append(line[0:-1])

i = 0
while i < len(names):
	without = copy.copy(names)
	without.pop(i)
	if names[i] in without:
		# duplicate found
		names.pop(i)
		text.pop(i)
	else:
		i += 1


with open("training.txt", "w") as f:
	for t in text:
		f.write(t + "\n")