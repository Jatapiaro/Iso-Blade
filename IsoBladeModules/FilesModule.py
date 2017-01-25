import numpy as np
import pickle
import csv
import os
np.set_printoptions(suppress=True)

def save_blade(blade,file_name,path):
    file_name += ".ibd"
    path += "/" + file_name
    pickle._dump(blade, open(path, "wb"))
    return path

def update_blade(blade,path):
    pickle._dump(blade,open(path,"wb"))
    return path

def load_blade(path):
    pass

def load_profile(path):

    x_points = []
    y_points = []

    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:
            x = float(row[0])
            y = float(row[1])
            x_points.append(x)
            y_points.append(y)

    return np.array(x_points),np.array(y_points)


