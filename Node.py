from utils import *
from Bridge import *

class Node:
    """
    This class specifies an "autoregulon"  node. (See my book Bayesuvius for
    more info about autoregulons)


    Attributes
    ----------

    gene: str
        name of Node. Usually the name of a gene.
    list_name_to_bridges: dict[str, list[Bridge]]
        A dictionary mapping the name of a list of Bridge's to the list of
        Bridge's. Such list names can be anything but are usual chosen to
        include the names of the two dags or recs that were combined to
        create self.

    """
    def __init__(self, gene, list_name_to_bridges=None):
        """
        Constructor
        
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
        This magic method returns a string describing an instance of this
        class any time that instance occurs in print()
        
        Returns
        -------
        str

        """
        return f"{self.gene}-node"

    @staticmethod
    def node_with_this_gene(nodes, gene):
        """
        This method returns a Node in the node list `nodes` if a Node that
        has the gene `gene` exists in the list. If no such Node exists,
        the method returns None.

        Parameters
        ----------
        nodes: list[Node]
        gene: str

        Returns
        -------
        Node

        """
        for node in nodes:
            if node.gene == gene:
                return node
        return None

    @staticmethod
    def merge_two_nodes(nd1, nd2):
        """
        This method returns a Node which merges Node's nd1 and nd2.
        
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

    def describe_self(self, long_desc=True):
        """
        This method prints a description of the Dag self. It writes a long
        description iff long_desc==True

        Parameters
        ----------
        long_desc: bool
            Set this to True (False) iff you want a long (short) description,

        Returns
        -------
        None

        """
        print("gene=", self.gene)
        if long_desc:
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

        list_name_to_bridges_x = {"rec_x": bridges}
        nd_a = Node("gg",
                    list_name_to_bridges_x)
        print("nd_a:")
        nd_a.describe_self()

        list_name_to_bridges_y = {"rec_y": bridges}
        nd_b = Node("gg",
                    list_name_to_bridges_y)
        print("nd_b:")
        nd_b.describe_self()

        nd_ab = Node.merge_two_nodes(nd_a, nd_b)
        print("nd_ab:")
        nd_ab.describe_self()
    main()