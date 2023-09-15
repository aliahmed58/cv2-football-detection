import cv2
import numpy as np
from matplotlib import pyplot as plt
from math import *

def angle_trunc(a):
    while a < 0.0:
        a += pi * 2
    return a

def getAngleBetweenPoints(x_orig, y_orig, x_landmark, y_landmark):
    deltaY = y_landmark - y_orig
    deltaX = x_landmark - x_orig
    return degrees(angle_trunc(atan2(deltaY, deltaX)))

# read the original image
cap = cv2.VideoCapture('./res/test_video.mp4')

while cap.isOpened():
    
    ret, original_image = cap.read()
    print(ret)
    
    # if ret == True:
    #     # convert image to hsv from BGR (default)
    #     hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

    #     # define range of red color in HSV
    #     lower_green = np.array([50, 100, 100])
    #     upper_green = np.array([90, 255, 255])   

    #     # threshold the HSV image to get only red colors
    #     green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    #     # remove the non green parts from the original frame
    #     green_only_image = cv2.bitwise_and(original_image, original_image, mask = green_mask)

    #     # apply canny edge algorithm 
    #     edges = cv2.Canny(green_only_image, 100, 300)
    #     lines = cv2.HoughLinesP(edges,3,np.pi/180,100,minLineLength=100,maxLineGap=10)

    #     verticals = []

    #     # for line in lines:
    #     #     x1,y1,x2,y2 = line[0]
    #     #     # angle = getAngleBetweenPoints(x1, y1, x2, y2)
    #     #     angle = getAngleBetweenPoints(x2, y2, x1, y1)
            
    #     #     if angle < 160:
    #     #         verticals.append(line[0])
    #     #         cv2.line(green_only_image,(x1,y1),(x2,y2),(0,255,255),3)


    #     cv2.imshow('Output', green_only_image)
    # else:
    #     break
    if ret == True:
        cv2.imshow('Output', original_image)


cap.release()
cv2.destroyAllWindows()