from Point import *

class Bridge:
    """

    Attributes
    ----------
    pt1: Point
    pt2: Point
    t1: int
    t2: int

    """
    def __init__(self, t1, pt1, t2, pt2):
        """

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

        Returns
        -------
        str

        """
        return f"{self.t1}{self.pt1}----{self.t2}{self.pt2}"
    
    @staticmethod
    def get_str(bridges):
        """

        Parameters
        ----------
        bridges: list[Bridge]

        Returns
        -------
        str

        """
        str1 = "t1(x1, xdot1)----t2(x2, xdot2)\n"
        for bridge in bridges:
            str1 += str(bridge) + "\n"
        return str1

if __name__ == "__main__":
    def main():
        pt = Point(.4555555, .8999999)
        bridge1 = Bridge(10, pt,20 , pt)
        bridge2 = Bridge(30, pt, 40, pt)
        bridges = [bridge1, bridge2]
        print(bridge1)
        print()
        print(Bridge.get_str(bridges))

    main()
