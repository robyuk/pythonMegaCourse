
"""Day 14 Coding Exercise 1
Create a function that finds out the state of water (i.e., gas, liquid, solid)
given the temperature. In other words, the function has a temperature parameter
and returns either "Gas", "Liquid" or "Solid" as a string depending on the temperature.
The function should be written in a separate file from the command line interface file.
The output should look like in the screenshot below:

    Enter water temperature:  -12
    Solid

Let's run it one more time. Here is another example:

    Enter water temperature:  100
    Gas

Note: To check if a value is between two values, you can use elif 0 < x < 100:

Solution"""
from exercises.waterstatefunction import water_state

temp = float(input("Enter water temperature: "))
print(water_state(temp))

"""Coding Exercise 2
In coding exercise 1, we hardcoded the values 0 and 100. 
It is better to change them to constants in the script where the function is defined. 
Therefore, your task is to modify the script from exercise 1 by creating two global 
variables/constants in that file, one variable associated with 0 and another associated with 100. 
Then, use those variables in the function instead of the values.

Solution"""
from exercises.waterstatefunction import water_state2

temp = float(input("Enter water temperature: "))
print(water_state(temp))

"""Bug-Fixing Exercise 1
The program depicted below consists of two Python files. The program tries to count and print out the number of periods in the "Trees are good. Grass is green." . However, running the main.py file returns an error. Please fix the error.

main.py:

import functions14
 
nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)


functions14.py:

def count(phrase):
    return phrase.count('.')
    
Solution
main.py:"""

import functions14

nr_of_periods = functions14.count("Trees are good. Grass is green.")
print(nr_of_periods)

"""functions14.py file is unchanged

Bug-Fixing Exercise 2
The same program as in exercise 1 now is throwing yet another error. Hunt the error down and fix it.

main.py:

import functions14.py
 
nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)


functions14.py:

def count(phrase):
    return phrase.count('.')

Solution
Again, functions14.py file is unchanged

main.py:"""
import functions14

nr_of_periods = functions14.count("Trees are good. Grass is green.")
print(nr_of_periods)

"""Bug-Fixing Exercise 3
There is another error in the same program. Please fix the error.

main.py:

from functions14 import count
 
nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)


functions14.py:

def count(phrase):
    return phrase.count('.')

Solution

Again, functions14.py is unchanged


main.py:"""
from functions14 import count

nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)
