from Node import *
from Arrow import *

class Dag:
    def __init__(self, arrows=None, nodes=None):
        if not arrows:
            self.arrows = []
        else:
            self.arrows = arrows
        if not nodes:
            self.nodes = []
        else:
            self.nodes = nodes

    def node_with_this_gene(self, gene):
        for node in self.nodes:
            if node.gene == gene:
                return node
        return None

    def update_arrow(self, start_g, end_g, accept):
        updated = False
        for ar in self.arrows:
            if ar.recognize_ends(start_g, end_g):
                if accept:
                    ar.accept()
                else:
                    ar.reject()
                updated = True
                break
        if not updated:
            ar1 =Arrow(start_g, end_g)
            self.arrows.append(ar1)
            if accept:
                ar1.accept()
            else:
                ar1.reject()

    def update_node(self, gene, rec1, rec2, acc_bridge):

        name = f"{rec1.name}&{rec2.name}"
        nd1 = None
        for nd in self.nodes:
            if gene == nd.gene:
                nd1 = nd
                break
        if not nd1:
            nd1 = Node(gene)
        if name not in nd1.comparison_to_bridges.keys():
            nd1.comparison_to_bridges[name] = []
        if acc_bridge is not None:
            nd1.comparison_to_bridges[name].append(acc_bridge)

