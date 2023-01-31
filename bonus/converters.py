def convert(feetinches):
    """ Accepts a dict in the format {'feet': feet, 'inches', inches}
    and returns the measure in meters as a float"""
    meters = float(feetinches["feet"]) * 0.3048 + float(feetinches["inches"]) * 0.0254
    return meters


if __name__ == "__main__":
    print("Function definition file for value conversions")
    print("convert({'feet': 6, 'inches': 7}) returns", convert({'feet': 6, 'inches': 7}))
