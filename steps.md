1. Use a yolo or any other neural net to detect the player and football. 
2. Use distance between center of box and ball to determine which player has the ball. The least distance is the one w possession. Set a min threshold.
3. Color mask the players detected (openCV lib) and check if the player's HSV range is above the threshold of that mentioned in the config file. This identifies which team the player belongs to.
4. After applying color filtering (NON GREEN FILTER TO remove non field areas), use canny edge detection algorithm on the image. 
5. Use hough transform to detect the halfway line so we can know where the ball is.
