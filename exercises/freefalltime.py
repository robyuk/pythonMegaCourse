"""Calculates the free fall time of an object
neglects the friction caused by the atmosphere"""

def calc_time(h, g=9.80665):
    """Accepts the height in meters and gravity as floats.
    Returns the time in seconds that it takes to fall that height"""
    t = (2 * h / g) ** 0.5
    return t


time = calc_time(100)
print(time)