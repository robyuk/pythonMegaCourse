"""Day 13 Coding Exercise 1
Define a function that has two parameters, year_of_birth and current_year .
The current_year parameter should be a default parameter with the current year as a default value.

The function should calculate and return the age of the user given the year of birth and the current year.

Note: It is enough to define the function for this exercise -no need to call it.

Solution"""

def calc_age(year_of_birth, current_year=2023):
    "Accepts year of birth and current year, both as int.  Returns the age as int"
    return current_year - year_of_birth


"""Coding Exercise 2
Your task for this exercise is to use the function you created in exercise 1. 
Then, below the function definition, get the year of birth from the user using an input function 
and then call and print the defined function to get the user's age as output. 

Solution"""
yob = int(input("What is your year of birth? "))
age = calc_age(yob)
print("Your age is", age)
"""Coding Exercise 3
Extend the program you wrote in exercise 2 by printing a message to the user 
instead of their age if their age is greater than 120. 
Feel free to print any message that you like.

Solution"""
if age > 120:
    print("That's really very old!")


"""Coding Exercise 4
Write a program that gets a list of names from the user and returns the number of names given. 
You are encouraged to use a function. Here is how the program would work:

    Enter names separated by commas (no spaces): john,jay,mary
    3

Solution"""
nameStr = input("Enter names separated by commas (no spaces): ")

def num_of_names(names=nameStr):
    """Accepts a string containing names separated by commas
    Returns the number of names as int"""
    nameList = names.split(',')
    return len(nameList)


print(num_of_names(nameStr))