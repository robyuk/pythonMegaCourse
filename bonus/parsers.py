def parse(feetinches):
    """ Accepts a string in the format 'feet inches' and returns a dict {'feet': feet, 'inches', inches}
    where the values are float"""
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


if __name__ == "__main__":
    print("Function definition file for parsing strings")
    print(f"parse('6 8') returns {parse('6 8')}")