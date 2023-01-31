"""
Implements a simple password check using defined functions and a list of booleans
"""
def contains_numbers(text):  # Checks if text contains number characters
    for i in text:
        if i.isdigit():
            return True
    return False


def contains_upper(text):  # Checks if text contains uppercase characters
    for i in text:
        if i.isupper():
            return True
    return False

def contains_lower(text):  # Checks if text contains lowercase characters
    for i in text:
        if i.islower():
            return True
    return False



password = input("Password: ")
result = []
if len(password) > 7:
    result.append(True)
else:
    result.append(False)

result.append(len(password) > 7)
result.append(contains_numbers(password))
result.append(contains_lower(password))
result.append(contains_upper(password))

if all(result):
    print("Strong password")
else:
    print("Weak password")