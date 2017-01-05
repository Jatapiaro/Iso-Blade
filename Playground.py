from Models.Point import Point
from Models.Profile import Profile
import numpy as np
import matplotlib.pyplot as plt
import csv

np.set_printoptions(suppress=True)

p = Profile()
points_up = []
points_down = []


"""
We used python csv instead of numpy to sort all the data,
the next step is to convert all the point list in a numpy ndarray
"""

with open('/Users/jacobotapia/Desktop/sorted.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    for row in readCSV:
        x = float(row[0])
        y = float(row[1])
        if x != 1 and y != 0:
            if y >= 0:
                points_up.append(Point(x, y))
            else:
                points_down.append(Point(x, y))


x_coordinates = []
y_coordinates = []

points_up.sort()
points_down.sort()
points_up.reverse()

points = points_up + points_down

points.append(Point(float(1),float(0)))
points.insert(0,Point(float(1),float(0)))

for point in points:
    x_coordinates.append(point.x)
    y_coordinates.append(point.y)

numpy_coordinates_x = np.array(x_coordinates)
numpy_coordinates_y = np.array(y_coordinates)

p.x_coordinates = numpy_coordinates_x
p.y_coordinates = numpy_coordinates_y

st = np.column_stack((numpy_coordinates_x,numpy_coordinates_y))

plt.plot(p.x_coordinates,p.y_coordinates)

plt.show()
