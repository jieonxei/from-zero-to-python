# List Less than Ten
# Exercise 3
# Take a list and write a program that prints out all the elements of the list that are less than 5.

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# This is a list of numbers stored in variable "a"

b = []
# This creates an empty list called "b"
# We will store numbers that meet a condition here

for x in a:
# This loop goes through each number in list "a" one by one
# Each number is temporarily stored in variable "x"

    if x < 5:
    # This checks if the current number is less than 5

        b.append(x)
        # If the condition is true, the number is added to list "b"

print(b)
# After the loop finishes, we print the final list "b"
# This shows only numbers from "a" that are less than 5

