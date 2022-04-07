# Take two lists and write a program that returns a list that contains only the elements that are common between the lists (w/o duplicates)

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

seta = set(a)
setb = set(b)

c = seta.intersection(setb)

print(c)

# Do this with random lists

aa = random.sample(range(10), 5) # 5 random integers from 0 to 9 
bb = random.sample(range(10), 5)

setaa = set(aa)
setbb = set(bb)
print(setaa)
print(setbb)

cc = setaa.intersection(setbb)
print(cc)
