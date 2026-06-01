# List Overlap
# Exercise 5
# write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

# Extras
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# First list of numbers
a = [1, 1, 2, 3, 5, 8, 13, 21]

# Second list of numbers
b = [1, 2, 3, 5, 8, 13, 34, 55]

# Empty list to store numbers that are in both lists
common = []

# Loop through each number in list a
for item in a:

    # Check two things:
    # 1. The number exists in list b
    # 2. The number is not already in common
    if item in b and item not in common:

        # Add the number to the common list
        common.append(item)

# Print the final list of common numbers
print(common)