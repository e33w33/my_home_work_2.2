import math
pi = math.pi


def circle_area(radius):
    try:
        radius = float(radius)
    except TypeError:
        raise ValueError()

    if radius < 0:
        return 'Радиус сферы не может быть отрицательным'
    return 4/3*pi*radius**3

