import copy

file = "training.txt" # change to testing.txt if you want to
names = []
text = []

print(f"file: {file}")
with open(file) as f:
	for line in f.readlines():
		names.append(line[1:-1])
		text.append(line[0:-1])
dupes = 0
i = 0
while i < len(names):
	without = copy.copy(names)
	without.pop(i)
	if names[i] in without: # duplicate found
		names.pop(i)
		text.pop(i)
		dupes += 1
	else:
		i += 1
	print(f"\r[{'#'*int(20*i/len(names))}{'-'*int(20-(20*i/len(names)))}] ({i}/{len(names)})  {dupes} duplicate(s)", end=" ")

with open(file, "w") as f:
	for t in text:
		f.write(t + "\n")

print(f"\n{dupes} duplicate(s) found!")
