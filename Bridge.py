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

    @staticmethod
    def merge_two_bridges_dicts(dict1, dict2):
        """
        This method returns a dictionary obtained by merging two dictionaries.
        The dictionaries are name_list_to_bridges

        Parameters
        ----------
        dict1: dict
        dict2: dict

        Returns
        -------
        dict

        """
        for name in dict1.keys():
            if name in dict2.keys():
                # print_list(dict1[name])
                # print_list(dict2[name])

                # the two list are the same.
                # won't check that whole thing is the same
                # just that their length and first elements are
                assert len(dict1[name]) == len(dict2[name])
                assert dict1[name][0].t1 == dict2[name][0].t1
                assert dict1[name][0].t2 == dict2[name][0].t2
        x = cp.deepcopy(dict1)
        x.update(dict2)
        return x


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
