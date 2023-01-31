"""
Coding Exercise 1
Please download the essay.txt file from the resources of this article.
Then, create a program that reads that file and prints out its text.
The first letter of each word in the output should be uppercase.
"""
filename = "files/essay.txt"

with open(filename, 'r') as file:
    content = file.read()
print(content.title(), '\n')

"""
Coding Exercise 2
Write a program that reads the essay.txt file and returns the number of characters contained in the file.
"""

print(f"The number of characters is", len(content))

"""
Coding Exercise 3
Please download the members.txt file from the resources of this article.

Then, create a program that, whenever executed, asks the user to enter a new member 
in the command line:

    Add a new member: Soloman Right

Then, the member is added to members.txt. 
In this case, the text file content would be:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right

Solution:  """

filename = "files/members.txt"
with open(filename, 'r') as file:
    members = file.read()
print(members)

newMember = input("Add a new member: ")
with open(filename, 'a') as file:
    file.write(newMember.title() + '\n')
print('\n')

"""Coding Exercise 4
Create a program that generates multiple text files by iterating over the filenames list. 
The text Hello should be written inside each generated text file.

Solution: """
filenames = [f"file{str(n)}" for n in range(5)]

for filename in filenames:
    with open(f"files/{filename}.txt", "w") as file:
        file.write("Hello")

"""Coding Exercise 5
Please download the three text files a.txt, b.txt, and c.txt from the resources. 
Then, create a program that reads each text file and prints out the content of 
each in the command line. 
"""
filenames = ["a", "b", "c"]
for filename in filenames:
    with open(f"files/{filename}.txt", "r") as file:
        print(file.read(), '\n')