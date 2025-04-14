from utils import *


class Node:
    def __init__(self, gene, comp_label_to_bridges=None):
        self.gene = gene
        if not comp_label_to_bridges:
            self.comp_label_to_bridges = {}
        else:
            self.comp_label_to_bridges = comp_label_to_bridges

    @staticmethod
    def merge_two_nodes(nd1, nd2):
        assert nd1.gene == nd2.gene
        return merge_two_dicts(nd1.comp_label_to_bridges,
                               nd2.comp_label_to_bridges)
