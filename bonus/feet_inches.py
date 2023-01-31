""" Inputs feet and inches in the format feet inches
and converts to meters"""
from bonus.converters import convert
from bonus.parsers import parse

if __name__ == "__main__":
    feet_inches = input("Enter feet inches: ")
    parsed = parse(feet_inches)
    result = convert(parsed)
    print(f"{parsed['feet']} feet and {parsed['inches']} inches is {result}m")
