def calculate_average_velocity(*args):
    velocity_sum = 0
    for i in args:
        try:
            velocity_sum += i
        except TypeError:
            raise TypeError()
    return velocity_sum / len(args)

