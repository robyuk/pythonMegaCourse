"""
Implements a simple password check using defined functions and a dictionary of booleans
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
result = {}

result["length > 7"] = len(password) > 7
result["numbers"] = contains_numbers(password)
result["lowercase"] = contains_lower(password)
result["uppercase"] = contains_upper(password)

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")
    print(result)
    exit(1)