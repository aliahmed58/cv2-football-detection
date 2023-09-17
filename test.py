import cv2
from pipeline import Pipeline
import pandas as pd
import math


frame = cv2.imread('./res/fifa.png')

pip = Pipeline()

halfway_line = pip._get_halfway_line(frame)

x1, y1, x2, y2 = halfway_line
center = [int((x1 + x2) / 2), int((y1 + y2) / 2)]

output = pip.draw_halfway_line(frame, halfway_line)

def draw_rect(image, start_point, end_point):
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    cv2.rectangle(image, start_point, end_point, color, thickness)

# def draw_lines_to_center = 

df = pd.read_csv('./res/test_4.csv')

out = pd.DataFrame()

slopes = []
distances = []
intercepts = []


for index, row in df.iterrows():
    start_point = (int(row['xmin']), int(row['ymin']))
    end_point = (int(row['xmax']), int(row['ymax']))
    
    center_of_box = (int((start_point[0] + end_point[0]) / 2), int((start_point[1] + end_point[1]) / 2))
    
    x1, y1 = center_of_box
    x2, y2 = center

    
    cv2.circle(output, (center_of_box), 4, (0, 0, 255), 5)
    
    # draw line from center to player center
    cv2.line(output, (x1, y1), (x2, y2), (0, 0, 0), 2)

    # get slope of line
    slope = (y2 - y1) / (x2 - x1)
    distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    alpha = math.atan2(y2 - y1, x2 - x1)
    
    
    slopes.append(slope)
    distances.append(distance)
    intercepts.append(alpha)
    
    
    draw_rect(output, start_point, end_point)
 
out['slope'] = slopes
out['distance'] = distances
out['alpha'] = intercepts

out.to_csv('./res/orig.csv', index=False)
 

print(center)
cv2.circle(output, (1001, 500), 4, (0, 0, 255), 5)


imS = cv2.resize(output, (960, 540))     
cv2.imshow('output', imS)



cv2.waitKey(0)
cv2.destroyAllWindows()