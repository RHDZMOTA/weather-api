
import math


def degree_to_radian(degree):
    return 2 * degree * math.pi / 360


def harversine(initial_coord, final_coord):
    # Distance between two coordinates (in km).
    r = 6371
    initial_rads = list(map(degree_to_radian, initial_coord))
    final_rads = list(map(degree_to_radian, final_coord))
    delta_phi = final_rads[0] - initial_rads[0]
    delta_lambda = initial_rads[1] - final_rads[1]
    h = math.sin(delta_phi/2) ** 2 + \
        math.cos(initial_rads[0]) * math.cos(final_rads[0]) * \
        math.sin(delta_lambda / 2) ** 2
    return 2*r*math.asin(math.sqrt(h))


