from math import pi


def area(radius):
    if type(radius) not in [int, float]:
        raise TypeError('Not an Integer or a Float type.')

    if radius < 0:
        raise ValueError('Radius is less than 0.')
    return pi*(radius**2)
