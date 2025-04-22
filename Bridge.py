from yaml.constructor import Constructor

from Point import *
from utils import *


class Bridge:
    """
    This class stores a "causal bridge", specified by two Point's pt1, pt2,
    and their respective times t1, t2.

    Attributes
    ----------
    pt1: Point
    pt2: Point
    t1: int
    t2: int

    """

    def __init__(self, t1, pt1, t2, pt2):
        """
        Constructor

        Parameters
        ----------
        t1: int
        pt1: Point
        t2: int
        pt2: Point
        """
        self.t1 = t1
        self.pt1 = pt1
        self.t2 = t2
        self.pt2 = pt2

    def __str__(self):
        """
        This magic method returns a string describing an instance of this
        class any time that instance occurs in print()

        Returns
        -------
        str

        """
        return f"{self.t1}{self.pt1}----{self.t2}{self.pt2}"


if __name__ == "__main__":
    def main():
        pt = Point(.4555555, .8999999)
        bridge1 = Bridge(10, pt, 20, pt)
        bridge2 = Bridge(30, pt, 40, pt)
        bridges = [bridge1, bridge2]
        print(bridge1)
        print()
        print("t1(x1, xdot1)----t2(x2, xdot2)")
        print_list(bridges)


    main()
