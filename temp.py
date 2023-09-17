import cv2
import pandas as pd

def draw_rect(image, start_point, end_point):
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    cv2.rectangle(image, start_point, end_point, color, thickness)

image = cv2.imread('./res/test_4.jpg')

df = pd.read_csv('./res/test_4.csv')

for index, row in df.iterrows():
    start_point = (int(row['xmin']), int(row['ymin']))
    end_point = (int(row['xmax']), int(row['ymax']))
    
    draw_rect(image, start_point, end_point)


cv2.imshow('output', image)
cv2.waitKey(0)
cv2.destroyAllWindows()