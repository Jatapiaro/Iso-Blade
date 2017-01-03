"""
The class Blade represents a collection of profiles
By now, the class is only saving Profiles

Args:
    profiles: A collection of profiles for a blade
"""
from Models.Profile import Profile

class Blade(object):

    def __init__(self, profiles=None):

        if profiles is None:
            profiles = []
        else:
            self.profiles = profiles


    def add_profile(self,profile):
        if profile is not None:
            self.profiles.append(profile)


    @property
    def profiles(self):
        return self.__profiles

    @profiles.setter
    def profiles(self,profiles):
        if profiles is None:
            self.__profiles = profiles
        else:
            self.__profiles = profiles

    def __repr__(self):
        str = ""
        for profile in self.profiles:
            str+=profile
        return str