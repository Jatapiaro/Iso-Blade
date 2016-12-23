"""
The class Profile represents a collection of points and a center for the profile

Args:
    points (List-->Points): List of points
    center (point): A Point that represent the center
"""

from Models.Point import Point
import numpy

class Profile(object):

    def __init__(self, center=None, x_coordinates=None, y_coordinates=None):

        if center is None:
            self.center = Point(0,0)
        else :
            self.center = center

        if x_coordinates is None:
            self.x_coordinates = numpy.array([])
        else:
            self.x_coordinates = x_coordinates

        if y_coordinates is None:
            self.y_coordinates = numpy.array([])
        else:
            self.y_coordinates = y_coordinates


    @property
    def x_coordinates(self):
        return self.__x_coordinates

    @x_coordinates.setter
    def x_coordinates(self,x_coordinates):
        if type(x_coordinates) is numpy.ndarray:
            self.__x_coordinates = x_coordinates
        else:
            self.__x_coordinates = numpy.array([])


    @property
    def y_coordinates(self):
        return self.__y_coordinates

    @y_coordinates.setter
    def y_coordinates(self,y_coordinates):
        if type(y_coordinates) is numpy.ndarray:
            self.__y_coordinates = y_coordinates
        else:
            self.__y_coordinates = numpy.array([])


    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self,center):
        if isinstance(center,Point):
            self.__center = center
        else:
            self.__center = Point(0,0)


    def __repr__(self):
        return "Center of profile: "+str(self.center)+"with points --> "+self.string_representation_of_points()


    def string_representation_of_points(self):
        return "Falta poner"



