# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

entry = input("Please enter a number: ")
num = int(entry)
test = range(1, num + 1)
list = []

for i in test:
    if (num % i) == 0: list.append(i)

print("The divisors of " + str(num) + " are " + str(list))
