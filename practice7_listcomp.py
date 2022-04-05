# Let's say you have a list as a variable. Write one line of Python that takes this 
# list and makes a new list that has only the even elements of this list.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = [i for i in a if i % 2 == 0]

print(even)
