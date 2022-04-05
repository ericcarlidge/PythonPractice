# Ask the user for a string and print out whether this string is a palindrome or not

string = input("Please enter a word: ")

if string == string[::-1]:
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome.")
