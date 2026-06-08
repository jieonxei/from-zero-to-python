# Exercise 13
# Filtering List with Conditional Logic
# Iterate through a given list of numbers and print only those numbers which are divisible by 5.

num_list = [10, 20, 33, 46, 55]
print("Given list is", num_list)
print("Divisible by 5:")

# Iterate through each element
for num in num_list:
    # Check divisibility
    if num % 5 == 0:
        print(num)