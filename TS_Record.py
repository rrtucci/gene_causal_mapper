from globals import *

class Point:
    def  __init__(self,
                  x,
                  xdot):
        self.x = x
        self.xdot = xdot

    @staticmethod
    def sim(pt1, pt2):
        if (abs(pt1.x-pt2.x) < X_RAD and
                abs(pt1.xdot - pt2.xdot) < XDOT_RAD):
            return True
        else:
            return False

class TS_Record:
    def __init__(self, name, times):
        self.name = name
        self.times = times
        self.gene_to_points =  None

    def check_self(self):
        for g, pts in self.gene_to_points.items():
            assert len(pts) == len(self.times)

