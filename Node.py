from utils import *
from Bridge import *

class Node:
    """
    Attributes
    ----------
    gene: str
    list_name_to_bridges: dict[str, list[Bridge]]

    """
    def __init__(self, gene, list_name_to_bridges=None):
        """
        
        Parameters
        ----------
        gene: str
        list_name_to_bridges: dict[str, list[Bridge]]
        """
        self.gene = gene
        if not list_name_to_bridges:
            self.list_name_to_bridges = {}
        else:
            self.list_name_to_bridges = list_name_to_bridges

    def __str__(self):
        """
        
        Returns
        -------
        str

        """
        return f"{self.name}-node"

    @staticmethod
    def merge_two_nodes(nd1, nd2):
        """
        
        Parameters
        ----------
        nd1: Node
        nd2: Node

        Returns
        -------
        Node

        """
        assert nd1.gene == nd2.gene
        dict12 = merge_two_dicts(nd1.list_name_to_bridges,
                               nd2.list_name_to_bridges)
        return Node(nd1.gene, dict12)

    def print_self(self):
        print("gene=", self.gene)
        print("list_name_to_bridges=")
        print_dict(self.list_name_to_bridges)

if __name__ == "__main__":
    def main():
        pt = Point(.4555555, .8999999)
        bridge1 = Bridge(10, pt,20 , pt)
        bridge2 = Bridge(30, pt, 40, pt)
        bridges = [bridge1, bridge2]
        print("bridge1=\n", bridge1)
        print()
        print("bridges=")
        print_list(bridges)

        list_name_to_bridges_12 = {"rec_12": bridges}
        nd_a = Node("gg", list_name_to_bridges_12)
        print("nd_a:")
        nd_a.print_self()

        list_name_to_bridges_23 = {"rec_23": bridges}
        nd_b = Node("gg", list_name_to_bridges_23)
        print("nd_b:")
        nd_b.print_self()

        nd_ab = Node.merge_two_nodes(nd_a, nd_b)
        print("nd_ab:")
        nd_ab.print_self()
    main()