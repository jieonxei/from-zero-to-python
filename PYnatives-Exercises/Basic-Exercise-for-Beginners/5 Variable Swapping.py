# Exercise 5
# Variable Swapping
# Write a program to swap the values of two variables, a and b, without using a third temporary variable.

a = 5
b = 10

print(f"Before Swap: a = {a}, b = {b}")

# this unpack the values of a and b and prevents it from being overwritten
a, b = b, a

print(f"After Swap: a = {a}, b= {b}")

