# String List
# Exercise 6
#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)

# Ask the user for a word
word = input("Enter a word: ")

# Reverse the word
reversed_word = word[::-1]

# Compare the original and reversed versions
if word == reversed_word:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
