contents=["All carrots are to be sliced "
           "longitudinally.",
          'The carrots were reportedly sliced',
          'The slicing process is well presented' ]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    with open(f"files/{filename}", 'w') as file:
        file.write(content)

string = "Strings can be concatenated " "by specifying multiple strings in the assignment"
print(string)

string = "A long string can be split " \
    "over multiple lines" \
    "using the backslash"

print(string)