import cv2
from pipeline import Pipeline

frame = cv2.imread('./res/test_4.jpg')

pip = Pipeline()

output = pip.halfway_lines(frame)

imS = cv2.resize(output, (960, 540))      

cv2.imshow('output', imS)

cv2.waitKey(0)
cv2.destroyAllWindows()