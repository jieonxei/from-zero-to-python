# Odd or Even
# Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num1 = int(input("Give me a number: "))
# Asks the user to type a number and converts it from text (string) into an integer

if num1 % 2 == 0:
# Checks if the number divided by 2 has no remainder
# If remainder is 0, the number is even

    print(f"The number {num1} is even")
    # Prints a message saying the number is even using an f-string

else:
# Runs this block if the condition above is false (meaning the number is NOT divisible by 2)

    print(f"The number {num1} is odd")
    # Prints a message saying the number is odd