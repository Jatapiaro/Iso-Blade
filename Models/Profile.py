"""
The class Profile represents a collection of points and a center for the profile

Args:
    points (List-->Points): List of points
    center (point): A Point that represent the center
"""

from Models.Point import Point

class Profile(object):

    def __init__(self, center=None, points=[]):

        if center is None:
            self.center = Point(0,0)
        else :
            self.center = center

        if points is None:
            self.points = []
        else :
            self.points = points

    def add_point(self,point):
        self.points.append(point)

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self,center):
        if isinstance(center,Point):
            self.__center = center
        else:
            self.__center = Point(0,0)

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self,points):
        if points is None:
            self.__points = []
        else:
            self.__points = points

    def __repr__(self):
        return "Center of profile: "+str(self.center)+" with points -->"+str(self.points)+"\n"

