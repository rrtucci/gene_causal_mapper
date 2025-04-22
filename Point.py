from globals import *


class Point:
    """
    This class stores a phase space point consisting of `x` and its time
    derivative `xdot`

    Attributes
    ----------
    x: float
    xdot: float
        time derivative of `x` at same time as `x`

    """

    def __init__(self, x, xdot):
        """
        Constructor

        Parameters
        ----------
        x: float
        xdot: float
        """

        self.x = x
        self.xdot = xdot

    def __str__(self):
        """
        This magic method returns a string (x, xdot) any time an instance of
        this class occurs in print()

        Returns
        -------
        str

        """
        return f"({self.x:{1}.{3}}, {self.xdot:{1}.{3}})"

    @staticmethod
    def are_sim(pt1, pt2):
        """
        This method returns True iff Point's pt1 and pt2 are at a small
        distance away from each other, in both, their x and xdot. How close
        they need to be so as to be considered similar (sim) is specified by
        the globals X_RAD and XDOT_RAD (RAD stands for radius).

        Parameters
        ----------
        pt1: Point
        pt2: Point

        Returns
        -------
        bool

        """
        if (abs(pt1.x - pt2.x) < X_RAD and
                abs(pt1.xdot - pt2.xdot) < XDOT_RAD):
            return True
        else:
            return False


if __name__ == "__main__":
    def main():
        pt = Point(.4555555, .8999999)
        print(pt)


    main()
