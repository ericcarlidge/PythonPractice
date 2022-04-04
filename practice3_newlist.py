# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

entry = input("Please enter a number in the range 1 to 90: ")
num = int(entry)

for i in a:
    if i < num: b.append(i)

print(b)
