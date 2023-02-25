from math import pi

from init.circle import circle


class Cylinder(circle):
    def _init_(self,radius,height):
        self.radius=radius
        self.height = height
    def volume(self):

        return pi*self.radius**2*self.height