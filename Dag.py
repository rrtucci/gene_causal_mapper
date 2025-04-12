from Demos.getfilever import pairs

from base_classes import *

class Dag:
    def __init__(self):
        self.arrows = []
        self.nodes = []

    def update_arrows(self, start_g, end_g, accept):
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

    def update_nodes(self, gene,  rec1, rec2, acc_bridge):
        updated = False
        for nd in self.nodes:
            if gene == nd.gene:
                nd.rec_pair_to_acc_bridge[(rec1, rec2)] =\
                    acc_bridge
                updated = True
                break
        if not updated:
            nd = Node(gene)
            nd.rec_pair_to_acc_bridge[(rec1, rec2)] = \
                acc_bridge
            


