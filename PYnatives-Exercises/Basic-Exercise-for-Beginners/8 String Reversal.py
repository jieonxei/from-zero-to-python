# Exercise 8
# String Reversal
#  Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

text = "Python"

reverse_word = text[::-1]

print(f"Original text: {text}")
print(f"Reversed: {reverse_word}")

#[::-1]: The first two colons imply “start at the very beginning” and “go to the very end.” The -1 indicates the direction of travel.