# Character Input 
# Exercise 1
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 

# Extras: (not done)
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

from datetime import datetime

name = input("What is your name? ")
age = int(input("How old are you? "))

current_year = datetime.now().year
year_for_100 = current_year + (100 - age)

print (name,", you will turn 100 years old in", year_for_100)