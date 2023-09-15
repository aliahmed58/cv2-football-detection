## Detecting Player's position on the field
1. Identifying the field area only and ignoring the rest from footage.
2. Figure out how much zoomed a camera is on the field / how much field is not currently shown in the frame.
3. What region of field is in the frame and how much of it out of the complete field. This is needed to find out player's relative position on the field.
4. Converting the x, y coordinates from side view to top down view.  

The input to the system are two video files, one of each half of the game. Ideally, the
recordings should be from a single camera, so if the recordings are of a TV-broadcast,
replays and closeups should be trimmed away. The system can cope with closeups to a
degree, because the players and ball will be too large for the neural network to detect, and
there will rarely be a line that is detectable. Replays, however, can cause be problematic
with the alternative angles that can cause the system to think it’s in the wrong half, not
to mention that it will count possession and other metrics during the replay. The impacts
from the replays have proven to be minimal during testing, but to get the most accurate
results, replays should be avoided.

Before the system is run some configuration is required. This is done in a config file that is
passed on into the program when run. The most important parameters that are specified
are:
• Path to the weights of the FootAndBall neural network
• Path to the input video files
• Names of the competing teams
• RGB value of a color that can uniquely identify one of the teams
• Which team that has the unique color (Home or Away)
• Which team that starts the game from the left half of the field (Home or Away)
• Output type (Realtime, video file, or none)
• Filename of the output video file, if needed