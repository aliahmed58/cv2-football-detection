""" All util functions go in this file """
import math
import numpy as np

def is_vertical(x1, y1, x2, y2) -> bool:
    delta_x = x2 - x1
    delta_y = y2 - y1
   
    if delta_x == 0:
        return False
    
    slope = abs(delta_y / delta_x)
    return slope > 1

def extend_line(line: np.ndarray, frame_height) -> list:
    
    # get the coordinates from list
    x1, y1, x2, y2 = line
    
    # calculate the equation of the line by getting the slope and intercept
    # y = mx + c
    delta_y = y2 - y1
    delta_x = x2 - x1
    
    slope = delta_y / delta_x
    intercept = y1 - (slope * x1)
    
    # use the equation to get coordinates of x extended when y = 0 and when y = frame_height
    # when y = 0
    x0 = int(-(intercept / slope))
    # when y = frame_height
    x3 = int((frame_height - intercept) / slope)
    
    return np.array([x0, 0, x3, frame_height])