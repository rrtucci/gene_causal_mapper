from globals import *


class Point:
    def __init__(self, x, xdot):
        self.x = x
        self.xdot = xdot

    def ___str___(self):
        return f"(x={self.x:{1}.{3}}, xdot={self.xdot:{1}.{3}})"

    @staticmethod
    def are_sim(pt1, pt2):
        if (abs(pt1.x - pt2.x) < X_RAD and
                abs(pt1.xdot - pt2.xdot) < XDOT_RAD):
            return True
        else:
            return False
