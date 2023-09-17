import numpy as np
import cv2
import config as cfg
import utils

# TODO: read configs like unique player color etc.

""" A generic python class to process each frame and apply the steps mentioned in pipeline """


class Pipeline():

    def __init__(self) -> None:
        pass

    # TODO: Use yolo to detect players and balls and return each frame with bounding box coordinates.
    def _yolo_detect(self) -> None:
        pass

    # TODO: Use yolo bounding box coordinates to calculate posession (which team, which player)
    def _get_posession(self) -> None:
        pass

    def _filter_field(self, frame: np.ndarray) -> np.ndarray:
        """
        Filter the noises from the frame such as players, audience etc and only keep green (field)
        Args:
            frame (np.ndarray): the frame in BGR format, should be read using imread
        Returns:
            np.ndarray: The numpy array that contains the field with only green color reamining
        """
        # convert the frame from BGR to HSV
        hsv_frame: np.ndarray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # threshold the frame to get only green colors
        green_mask: np.ndarray = cv2.inRange(
            hsv_frame, cfg.LOWER_GREEN, cfg.UPPER_GREEN)

        # get the green only part from the image
        green_only_frame: np.ndarray = cv2.bitwise_and(
            frame, frame, mask=green_mask)

        return green_only_frame

    def _detect_lines(self, green_only_frame: np.ndarray) -> np.ndarray:
        """
        Detect lines on the field so the halfway line and penalty lines can be filtered out from it
        Algorithms used: Canny Edge detection after green color masking and Hough Transform
        Args:
            green_only_frame (np.ndarray): green_only_frame that is previously filtered using _filter_field()
        Returns:
            np.ndarray: the array containing the lines 
        """

        # Apply canny edge algorithm to get edges only
        edges_in_frame: np.ndarray = cv2.Canny(green_only_frame, 100, 300)

        # apply probabilistic hough transform to get the array of lines
        lines: np.ndarray = cv2.HoughLinesP(
            edges_in_frame, rho=3, theta=np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

        return lines

    def _detect_filter_halfway_line(self, lines: np.ndarray) -> np.ndarray:
        """
        Among the lines detected in the frame, the halfway line is supposed to be vertical to the horizontal axis at some
        approximate angle which happens to be in the range of 70 - 100 (approx)
        Args:
            lines (np.ndarray): the array of lines filtered after they were detected in frame

        Returns:
            np.ndarray: array containing only the most probabilistic halfway lines
        """
        if lines is None:
            return None

        # array to save vertical lines
        vertical_lines = []

        # loop over all the lines detected
        for line in lines:
            # get start and end coordiantes of line
            x1, y1, x2, y2 = line[0]

            # check if the line is vertical or not (halfway line or not)
            vertical_test = utils.is_vertical(x1, y1, x2, y2)

            # if line is vertical append it to the list
            if vertical_test:
                vertical_lines.append(line[0])

        vertical_lines = np.asarray(vertical_lines)

        return vertical_lines
    
    def _get_halfway_line(self, frame: np.ndarray) -> np.ndarray:
        
        # get image height (frame)
        height, _ = frame.shape[:2]
        
        # get the green only frame using filter field method
        green_only_frame: np.ndarray = self._filter_field(frame)
        
        # detect lines on the frame
        all_lines: np.ndarray = self._detect_lines(green_only_frame)
        
        # get vertical lines from all the lines
        vertical_lines: np.ndarray = self._detect_filter_halfway_line(all_lines)
        
        # TODO: get the best possible vertical line that is over halfway to extend it instead of line[0]
        # extend the line and draw it on frame
        halfway_line = utils.extend_line(vertical_lines[0], height)
        
        return halfway_line
    
    def draw_halfway_line(self, frame: np.ndarray, line: np.ndarray) -> np.ndarray:
       
        x0, y0, x3, y3 = line 
        
        cv2.line(frame, (x0, y0), (x3, y3), (0, 255, 255), 3)
        
        center = (int((x0 + x3) / 2), int((y0 + y3) / 2))
        cv2.circle(frame, (center), 4, (255, 0, 0), 10)

        return frame
        
