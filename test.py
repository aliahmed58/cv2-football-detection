import cv2
from pipeline import Pipeline

frame = cv2.imread('./res/fifa_test.png')

pip = Pipeline()

output = pip._filter_field(frame)

imS = cv2.resize(output, (960, 540))      

cv2.imshow('output', imS)

cv2.waitKey(0)
cv2.destroyAllWindows()