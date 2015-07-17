Drunken Bishop
==============

A python tool to generate those funny images ssh generates when you connect to a new server or generate a new key. They are meant to give you a more visual representaion of a hash value.

```
+---[ECDSA 256]---+
|        o.=o o   |
|       *.*.o* .  |
|      + ==oB.o ..|
|     o  ..B.= ..o|
|    + . S..*... .|
|   . +    ..=o   |
|      o    o.o.  |
| E . . ..  .+    |
|  ..o  ....  o   |
+----[SHA256]-----+
```

The algorithm is best described here http://dirk-loss.de/sshvis/drunken_bishop.pdf from where the follwing paragraph is quoted.

```
Bishop Peter finds himself in the middle of an ambient atrium. There
are walls on all four sides and apparently there is no exit. The floor is
paved with square tiles, strictly alternating between black and white. His
head heavily aching—probably from too much wine he had before—he
starts wandering around randomly. Well, to be exact, he only makes
diagonal steps—just like a bishop on a chess board. When he hits a
wall, he moves to the side, which takes him from the black tiles to the
white tiles (or vice versa). And after each move, he places a coin on
the floor, to remember that he has been there before. After 64 steps,
just when no coins are left, Peter suddenly wakes up. What a strange
dream!
```

Example Usage
-------------
```
$ python drunken-bishop.py -M ~/.ssh/id_rsa.pub
+------[RSA]------+
|                 |
|                 |
|          .      |
|         . .     |
|    .  oS o      |
| . . o+o . o     |
|o o .o=    .o    |
| + ooo .  E  .   |
|..=o .. .. o     |
+------[MD5]------+

$ python drunken-bishop.py ~/.ssh/id_ecdsa.pub
+---[ECDSA 256]---+
|        o.=o o   |
|       *.*.o* .  |
|      + ==oB.o ..|
|     o  ..B.= ..o|
|    + . S..*... .|
|   . +    ..=o   |
|      o    o.o.  |
| E . . ..  .+    |
|  ..o  ....  o   |
+-----[SHA256]----+
```


How useful is this
------------------
The images are pretty much useless. I have never known anyone who looks at them.



