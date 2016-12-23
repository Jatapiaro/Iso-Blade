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



    def __lt__ (self, other):

        """Compare if a Point is greater than other.

        The criteria used in this method is that a profile file,
        must pass the points from (1,0) to (0,0) to (1,0),
        it means that first we need the points with positive 'y'
        and also verify which point has the greater 'x'

        Keyword arguments:
        other -- other point with x and y coordinates
        """
        return self.x < other.x and self.y < other.y

    def __gt__ (self, other):
        return other.__lt__(self)

    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y

    def __ne__ (self, other):
        return not self.__eq__(other)


    def __repr__(self):
        return "["+str(self.x)+","+str(self.y)+"]\n"
