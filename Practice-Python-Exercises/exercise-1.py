# Character Input 
# Exercise 1
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 

# Extras: (not done)
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# imports the datetime module to get the current year
from datetime import datetime  

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their age and convert it to an integer
age = int(input("How old are you? "))

# Get the current year automatically
current_year = datetime.now().year

# Calculate the year when the user will turn 100
# (100 - age) gives how many years are left until 100
year_for_100 = current_year + (100 - age)

# Print the final result
print(name, ", you will turn 100 years old in", year_for_100)