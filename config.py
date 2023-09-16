import numpy as np

# mask value ranges in HSV
# green lower and upper bounds
LOWER_GREEN: np.ndarray = np.array([50, 100, 100])
UPPER_GREEN: np.ndarray = np.array([90, 255, 255])
