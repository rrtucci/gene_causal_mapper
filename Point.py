from globals import *


class Point:
    """

    Attributes
    ----------
    x: float
    xdot: float

    """
    def __init__(self, x, xdot):
        """

        Parameters
        ----------
        x: float
        xdot: float
        """

        self.x = x
        self.xdot = xdot

    def __str__(self):
        """

        Returns
        -------
        str

        """
        return f"({self.x:{1}.{3}}, {self.xdot:{1}.{3}})"

    @staticmethod
    def are_sim(pt1, pt2):
        """

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