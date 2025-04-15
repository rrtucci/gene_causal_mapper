from Node import *
from Arrow import *

import graphviz as gv
from IPython.display import display, Image
from PIL.Image import open as open_image


class Dag:
    def __init__(self, arrows=None, nodes=None, title=None):
        if not arrows:
            self.arrows = []
        else:
            self.arrows = arrows

        if not nodes:
            self.nodes = []
        else:
            self.nodes = nodes

        if not title:
            self.title = ""
        else:
            self.title = title

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
            ar1 = Arrow(start_g, end_g)
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
        if nd1 is None:
            nd1 = Node(gene)
        if acc_bridge is not None:
            (nd1.comp_label_to_bridges.
                setdefault(name, []).append(acc_bridge))

    @staticmethod
    def draw_dot(s, j_embed):
        """
        This method draws a dot string.

        Using display(s) will draw the graph but will not embed it permanently
        in the notebook. To embed it permanently, must generate temporary image
        file and use Image().display(s)

        Parameters
        ----------
        s: output of graphviz Source(dot_str)
        j_embed: bool
            True iff want to embed image in jupyter notebook. If you are
            using a python terminal instead of a jupyter notebook,
            only j_embed=False will draw image.

        Returns
        -------
        None
        """
        x = s.render("tempo", format='png', view=False)
        if j_embed:
            display(Image(x))
        else:
            open_image("tempo.png").show()

    def draw(self,
             prob_acc_thold,
             num_trials_thold,
             jupyter=False):
        """
        This method draws the graph for self. Only arrows with
        `prob_acceptance` >= `prob_acc_thold` are drawn.

        Parameters
        ----------
        prob_acc_thold: float
        num_trials_thold: int
        jupyter: bool

        Returns
        -------
        None

        """
        ars = self.arrows
        hprob_arrows = []
        for ar in ars:
            if ar.above_thresholds(prob_acc_thold,
                                   num_trials_thold):
                hprob_arrows.append(ar)

        dot = "digraph {\n"
        for arrow in hprob_arrows:
            prob_acc = arrow.get_prob_acc()
            nsam = arrow.get_num_trials()
            X = f'{str(prob_acc)}({str(nsam)})'
            dot += f"{arrow.start_g}->{arrow.end_g}[label={X}];\n"
        dot += 'labelloc="b";\n'
        dot += 'label="' + self.title + '";\n'
        dot += "}\n"
        # print("vvbn", dot)
        Dag.draw_dot(gv.Source(dot), j_embed=jupyter)
