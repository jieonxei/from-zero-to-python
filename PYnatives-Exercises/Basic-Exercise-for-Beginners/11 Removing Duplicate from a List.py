# Exercise 11
# Removing duplicate from a list
# Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

data = [1, 2, 2, 3, 4, 4, 4, 5]

# Set conversion removes duplicates automatically
unique_data = list(set(data))

print(f"Unique List: {unique_data}")

# set(data): A Set is a collection where every element must be unique. 
# When you pass a list into a set, Python automatically discards any value it has already seen.