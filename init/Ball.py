from math import pi

from init.circle import circle


class Ball(circle):
    def volume(self):
        v = (4 / 3) * pi * self.radius ** 3
        return v

    def area(self):
        return 4 *pi*self.radius ** 2
    def print_area(self):
        print("the area is" + str(super().area()))

