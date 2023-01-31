def water_state(temperature):
    """ Accepts temperature as float and returns a string as follows:
    'Solid' if water is frozen at that temperature
    'Liquid' if water is liquid at that temperature
    'Gas' if the temperature is at or above the boiling point of water"""
    if 0 < temperature < 100:
        return "Liquid"
    elif temperature <= 0:
        return "Solid"
    elif temperature >= 100:
        return "Gas"
    else:
        raise(ValueError)


boilingpoint=100
freezingpoint=0

def water_state2(temperature):
    """ Accepts temperature as float and returns a string as follows:
    'Solid' if water is frozen at that temperature
    'Liquid' if water is liquid at that temperature
    'Gas' if the temperature is at or above the boiling point of water"""
    if freezingpoint < temperature < boilingpoint:
        return "Liquid"
    elif temperature <= freezingpoint:
        return "Solid"
    elif temperature >= boilingpoint:
        return "Gas"
    else:
        raise(ValueError)
