filenames = ['document', 'report', 'presentation']

for index, file in enumerate(filenames):
    print(f'{index}-{file.capitalize()}.txt')

ips = ['100.122.133.105', '100.122.133.111']


index = int(input("Enter the index number: "))
try:
    print(ips[index])
except IndexError:
    pass
