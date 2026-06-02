# Arithmetic Product and Conditional Logic
# Exercise 1
# Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

# defines a function named calculate (it accepts the number1&2)
def calculate(number1, number2):
    #then compute the two products
    product = number1 * number2

    #if the product is less than a thousand it will fall or return to the argument (+)
    if product <= 1000:
        return product
    else:
        return number1 + number2

print(calculate(20,30))
print(calculate(30,70))

