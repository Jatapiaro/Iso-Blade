"""
The class point represents the coordinates of a 2D point using x and y values.

Args:
    x (float): x value of the coordinate
    y (float): y value of the coordinate
"""
class Point(object):


    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        if isinstance(x,float):
            self.__x = x
        else:
            self.__x = 0

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        if isinstance(y,float):
            self.__y = y
        else:
            self.__y = 0


    def __repr__(self):
        return "["+str(self.x)+","+str(self.y)+"]\n"
