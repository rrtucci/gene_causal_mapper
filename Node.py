from utils import *

class Node:
    def __init__(self, gene, comparison_to_bridges=None):
        self.gene = gene
        if  not comparison_to_bridges:
            self.comparison_to_bridges = {}
        else:
            self.comparison_to_bridges = comparison_to_bridges

    @staticmethod
    def merge_two_nodes(nd1, nd2):
        assert nd1.gene == nd2.gene
        return merge_two_dicts(nd1.comparison_to_bridges,
                        nd2.comparison_to_bridges)