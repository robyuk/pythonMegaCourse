"""Coding Exercise 1 """

names = ["john smith", "jay santi", "eva kuki"]

"""
Extend the code above so the code capitalizes all the names and the surnames of the list and then prints the new list.

The output of your code should be as below:

['John Smith', 'Jay Santi', 'Eva Kuki']
Solution: """
capitalNames = [name.title() for name in names]
print(capitalNames)

"""Coding Exercise 2 """
usernames = ["john 1990", "alberta1970", "magnola2000"]

"""Extend the code above so the code prints out a list containing the number of characters for each username.

The output of your code should be as below:

[9, 11, 11]
Solution:  """
numbers = [len(name) for name in usernames]
print(numbers)

""" Coding Exercise 3 """
user_entries = ['10', '19.1', '20']
"""
Extend the code above so the code prints out a list containing the same items as floats.

The output of your code should be as below:

[10.0, 19.1, 20.0]
Solution:  """
user_entries = [float(user) for user in user_entries]
print(user_entries)

"""
Coding Exercise 4
user_entries = ['10', '19.1', '20']
Extend the code above so the code prints out the sum of the numbers.

The output of your code should be as below:

49.1
Hint: Use the sum() function. The function gets a list of numbers as input and produces the sum of all numbers. 
For more info, try help(sum).

Solution
"""
print(sum(user_entries))

"""Bug-Fixing Exercise 1
The code below tries to write the items of temperatures each in one line in the file.txt list. 
However, the code has an error. Try to fix the error.
"""
temperatures = [10, 12, 14]
file = open("file.txt", 'w')
temperatures = [str(temp) + '\n' for temp in temperatures]  # My fix, add this line
file.writelines(temperatures)

"""Bug-Fixing Exercise 2
The code below tries to convert all the numbers to integers. However, the code has an error. Try to fix the error.
"""

numbers = [10.1, 12.3, 14.7]
#numbers = [int(number) for item in numbers]  # Line with error
numbers = [int(item) for item in numbers]   # My fix
print(numbers)
