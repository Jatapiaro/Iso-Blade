from Models.Point import Point
from Models.Profile import Profile
import csv

p = Profile()

with open('/Users/jacobotapia/Desktop/circle.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    for row in readCSV:
        x = float(row[0])
        y = float(row[1])
        p.add_point(Point(x,y))


print(p)

