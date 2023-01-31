"""Day 10 Coding Exercise 1
Build a percentage calculator that gets from the user the "total value" and the "value"
and returns the percentage as shown below:

    Enter total? 50
    Enter value? 20
    That is 40.0%

The program should also print a message if the user doesn't enter a number for the "total"
or for the "value"

Coding Exercise 2
As you might know, it is not mathematically possible to divide a number by zero.
Consequently, this is also not possible in Python either, you will get a ZeroDivisionError if you try:

    >>> 20 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

With that in mind, your task for this exercise is to extend the program you created in Exercise 1
by displaying a message to the user when they enter 0 for the "total value"."""

print("Calculate the percentage of a total")

try:
    total = float(input("Enter total? "))
    value = float(input("Enter value? "))
except ValueError:
    exit("Please enter the value and total as numbers")

if total == 0:
    exit("Your total cannot be zero.")

percent = 100 * value / total
print(f"That is {percent}%")