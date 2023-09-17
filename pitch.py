from mplsoccer import Pitch
from matplotlib import pyplot as plt
import pandas as pd
import math
from sklearn.preprocessing import MinMaxScaler

plt.rcParams["figure.figsize"] = (10,6)

pitch = Pitch(pitch_color='grass', stripe = True, axis=True, label=True, tick=True)
print(pitch.pitch_width)
fig, ax = pitch.draw()

ax.set(xlim=(0, 120), ylim=(0, 80))

circle1 = plt.Circle((60, 40), 0.7, color='r')

plt.gca().add_patch(circle1)

data = pd.read_csv('./res/orig.csv')

rmin = 0
rmax = 1001

tmin = 0
tmax = 72

sdistance = []
slopes = list(data['slope'])
alpha = list(data['alpha'])

scaler = MinMaxScaler()
model = scaler.fit(data)
scaled_data = model.transform(data)

print(scaled_data)

for index, row in data.iterrows():
    distance = row['distance']
    
    scaled_distance = ((distance - rmin) / (rmax - rmin)) * (tmax - tmin) + tmin
    
    sdistance.append(scaled_distance)

print(sdistance)

points = []

for i in range(len(sdistance)):
    slope = slopes[i]
    d = sdistance[i]
    a = alpha[i]
    # a = abs(alpha[i]) if slope > 0 else alpha[i]
    # print(d)
    # c = 40 - slope * 60
    
    # y = mx + c
    c = 0
    x2 = 60 - d * math.cos(a)
    y2 = 40 - d * math.sin(a)
    # print(math.sqrt(pow(x2 - 60, 2) + pow(y2 - 40, 2)))
    
    points.append([int(x2), int(y2)])
    
print(points)
    
for p in points:
    
    circle1 = plt.Circle((p[0], p[1]), 0.7, color='b')
    
    plt.gca().add_patch(circle1)
    
    
plt.show()