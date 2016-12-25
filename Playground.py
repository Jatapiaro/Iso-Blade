from Models.Point import Point
from Models.Profile import Profile
import numpy as np
import csv

np.set_printoptions(suppress=True)

p = Profile()
points = []


"""
We used python csv instead of numpy to sort all the data,
the next step is to convert all the point list in a numpy ndarray
"""

with open('/Users/jacobotapia/Desktop/circle.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    for row in readCSV:
        x = float(row[0])
        y = float(row[1])
        points.append(Point(x,y))


x_coordinates = []
y_coordinates = []

for point in points:
    x_coordinates.append(point.x)
    y_coordinates.append(point.y)

numpy_coordinates_x = np.array(x_coordinates)
numpy_coordinates_y = np.array(y_coordinates)

p.x_coordinates = numpy_coordinates_x
p.y_coordinates = numpy_coordinates_y

st = np.column_stack((numpy_coordinates_x,numpy_coordinates_y))

print(p)