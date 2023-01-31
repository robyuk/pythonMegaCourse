import csv

with open("files/weather.csv", "r") as file:
    data = dict(csv.reader(file))

print(data)

city = input("City: ")
print(data[city])