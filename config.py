import numpy as np

# mask value ranges in HSV
# green lower and upper bounds
# TODO: figure out a proper green color range that works for all fields
LOWER_GREEN: np.ndarray = np.array([30, 100, 100])
UPPER_GREEN: np.ndarray = np.array([90, 255, 255])
