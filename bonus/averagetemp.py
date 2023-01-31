def get_average():
    with open("files/temperatures.txt", "r") as file:
        content = file.readlines()
    temperatures = [float(i) for i in content[1:]]
    avg = sum(temperatures) / len(temperatures)
    return avg


if __name__ == "__main__":
    average = get_average()
    print(average)