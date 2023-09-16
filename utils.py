""" All util functions go in this file """
import math

def is_vertical(x1, y1, x2, y2) -> bool:
    delta_x = x2 - x1
    delta_y = y2 - y1
    slope = abs(delta_y / delta_x)
    return slope > 2