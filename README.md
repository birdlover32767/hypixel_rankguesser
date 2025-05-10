# hypixel_rankguesser
uses tensorflow to guess hypixel ranks based on usernames

## data
if you inspect <code>training.txt</code>, you will see something like this:

```
5Steve
4Alex
0abcdefg
...
```

each line has 1 data point. the first character is the rank (0: non, 1: VIP, 2: VIP+, 3: MVP, 4: MVP+, 5: MVP++), and the rest is the username.

when running, the usernames get extra null characters to make them 20 and the unicode codepoints of each character minus 48 (<code>ord(character)-48</code>) are put in a numpy array.
