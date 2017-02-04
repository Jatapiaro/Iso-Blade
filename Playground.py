import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt
import csv
np.set_printoptions(suppress=True)

def bspline(cv, n=100, degree=3):
    """ Calculate n samples on a bspline

        cv :      Array ov control vertices
        n  :      Number of samples to return
        degree:   Curve degree
    """
    n+=1
    cv = np.asarray(cv)
    count = len(cv)

    factor, fraction = divmod(count+degree+1, count)
    cv = np.concatenate((cv,) * factor + (cv[:fraction],))
    count = len(cv)
    degree = np.clip(degree,1,degree)


    # Calculate knot vector
    kv = None
    kv = np.arange(0-degree,count+degree+degree-1,dtype='int')

    # Calculate query range
    u = np.linspace(True,(count-degree),n)


    # Calculate result
    arange = np.arange(len(u))
    points = np.zeros((len(u),cv.shape[1]))
    for i in range(cv.shape[1]):
        points[arange,i] = si.splev(u, (kv,cv[:,i],degree))

    return points

colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')


x_coordinates = []
y_coordinates = []
with open('/Users/jacobotapia/Desktop/otro.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    for row in readCSV:
        x = float(row[0])
        y = float(row[1])
        x_coordinates.append(x)
        y_coordinates.append(y)


numpy_coordinates_x = np.array(x_coordinates)
numpy_coordinates_y = np.array(y_coordinates)


st = np.column_stack((numpy_coordinates_x,numpy_coordinates_y))



cv = st


plt.plot(cv[:,0],cv[:,1], label='Control Points')

p = bspline(cv, n=10, degree=3)
x, y = p.T
plt.plot(x,y,'^',label='Degree %s'%3,color=colors[3%len(colors)])

st2 = np.column_stack((x,y))
print(st2)



plt.minorticks_on()
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

