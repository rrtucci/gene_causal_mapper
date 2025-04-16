from utils import *


class Node:
    def __init__(self, gene, comp_label_to_bridges=None):
        self.gene = gene
        if not comp_label_to_bridges:
            self.comp_label_to_bridges = {}
        else:
            self.comp_label_to_bridges = comp_label_to_bridges

    def __str__(self):
        str1 = ""
        str1 += self.gene + "\n"
        for comp_label, bridges in self.comp_label_to_bridges.item():
            str1 += comp_label + ":" + str(bridges) + "\n"
        return str1 

    @staticmethod
    def merge_two_nodes(nd1, nd2):
        assert nd1.gene == nd2.gene
        return merge_two_dicts(nd1.comp_label_to_bridges,
                               nd2.comp_label_to_bridges)
