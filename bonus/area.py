print("Calculate the area of a rectangle")

try:
    width = float(input("Width? "))
    length = float(input("Length? "))
except ValueError:
    exit("Please enter the width and length as numerics")

area = width * length
print("Area is:", area)