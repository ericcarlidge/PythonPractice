# Take two lists and write a program that returns a list that contains only the elements that are common between the lists.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    for j in b:
            if i == j: 
                c.append(i)
    
print(c)

# The below is another way to do this using 'set' and it handles duplicates.

sa = set(a)
sb = set(b)

print(sa) # unordered tuple of a
print(sb) # unordered tuple of b - prints ordered

sc = list(sa.intersection(sb))
print(sc)
