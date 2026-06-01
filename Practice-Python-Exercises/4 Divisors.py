# Divisors
# Exercise 4
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Give me a number: "))

divisors = []
# This list will store all numbers that divide evenly into "num"

for i in range(1, num + 1):
# This loop checks every number from 1 up to the number itself

    if num % i == 0:
    # If remainder is 0, it means i divides num evenly

        divisors.append(i)
        # Add i to the list of divisors

print("Divisors of", num, "are:", divisors)
# Print the final list of divisors