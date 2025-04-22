from Node import *
from Arrow import *

import graphviz as gv
from IPython.display import display, Image
from PIL.Image import open as open_image

import pickle as pkl


class Dag:
    """
    This class defines a DAG (Directed Acyclic Graph)


    Attributes
    ----------
    arrows: list[Arrow]
    nodes: list[Node]
    title: str

    """
    def __init__(self,
                 arrows=None,
                 nodes=None,
                 title=None,
                 in_path_of_pkl=None):
        """
        Constructor

        Parameters
        ----------
        arrows: list[Arrow]
        nodes: list[Node]
        title: str
        in_path_of_pkl: str|None
            path to  a pickle file that contains an instance of this class.
            This is path is optional. If given, then `self.arrows` and
            `self.nodes` are filled with the data in the pickle file.
        """
        if in_path_of_pkl:
            with open(in_path_of_pkl, "rb") as f:
                dag = pkl.load(f)
                self.arrows = dag.arrows
                self.nodes = dag.nodes
                self.title = dag.title
            return
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

    def save_self(self, dag_dir):
        """
        This method saves self as a pickle file. The file is saved in the
        directory `dag_dir`, with the title self.title + ".pkl"

        Parameters
        ----------
        dag_dir: str
            Directory in which pickled file is stored.

        Returns
        -------
        None

        """
        path = dag_dir + "/" + self.title + ".pkl"
        with open(path, "wb") as f:
            pkl.dump(self, f, protocol=pkl.HIGHEST_PROTOCOL)

    def update_node(self, gene, list_name, acc_bridge):
        """
        This method adds an accepted bridge `acc_bridge` to the list
        `list_name` of bridges, in the Node named `gene`

        Parameters
        ----------
        gene: str
        list_name: str
        acc_bridge: Bridge

        Returns
        -------
        None

        """

        updated = False
        for nd in self.nodes:
            if gene == nd.gene:
                nd1 = nd
                updated = True
                break
        if not updated:
            nd1 = Node(gene)
            self.nodes.append(nd1)
        if acc_bridge:
            (nd1.list_name_to_bridges.
             setdefault(list_name, []).append(acc_bridge))

    def update_arrow(self, start_g, end_g, accept):
        """
        This method updates the Arrow that points from gene `start_g` and to
        gene `end_g` in the Dag self. The method Arrow.accept() is called if
        accept==True, whereas the method Arrow.reject() is called if
        accept==False.

        Parameters
        ----------
        start_g: str
        end_g: str
        accept: bool

        Returns
        -------
        None

        """
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

    @staticmethod
    def draw_dot(dot_str, j_embed, circo=True):
        """
        This method draws a dot string.

        Using display(s) will draw the graph but will not embed it permanently
        in the notebook. To embed it permanently, must generate temporary image
        file and use Image().display(s)

        Parameters
        ----------
        dot_str: str
        j_embed: bool
            True iff want to embed image in jupyter notebook. If you are
            using a python terminal instead of a jupyter notebook,
            only j_embed=False will draw image.
        circo: bool
            Whether to draw the dag with the nodes on a circle (circo=True)
            or in topological order which is the graphviz default
            (circo=False)

        Returns
        -------
        None
        """
        if circo:
            src = gv.Source(dot_str, engine='circo')
        else:
            src = gv.Source(dot_str)
        x = src.render("tempo", format='png', view=False)
        if j_embed:
            display(Image(x))
        else:
            open_image("tempo.png").show()

    def draw(self,
             prob_acc_thold,
             num_trials_thold,
             jupyter=False,
             circo=True):
        """
        This method draws the graph for self. Only arrows ar with
        ar.prob_acceptance > prob_acc_thold and ar.num_trials>
        num_trials_thold and are drawn. thold=threshold

        Parameters
        ----------
        prob_acc_thold: float
        num_trials_thold: int
        jupyter: bool
        circo: bool

        Returns
        -------
        None

        """
        hprob_arrow_to_matched = {}
        for ar in self.arrows:
            if ar.above_thresholds(prob_acc_thold,
                                   num_trials_thold):
                matched = False
                for ar1 in hprob_arrow_to_matched:
                    if ar1.start_g == ar.end_g and ar1.end_g == ar.start_g:
                        matched = True
                        break
                hprob_arrow_to_matched[ar] = matched

        dot_str = "digraph {\n"
        for arrow in hprob_arrow_to_matched:
            prob_acc = arrow.get_prob_acc()
            num_trials = arrow.get_num_trials()
            X = f'"{prob_acc:{1}.{2}}({num_trials})"'
            ar_c_str = ""
            font_c_str = ""
            if hprob_arrow_to_matched[arrow]:
                ar_c_str = ", color=red"
                font_c_str = ", fontcolor=red"
            dot_str += (f"{arrow.start_g}->{arrow.end_g}[label={X}"
                        f"{ar_c_str}{font_c_str}];\n")
        dot_str += 'labelloc="b";\n'
        dot_str += 'label="' + self.title + '";\n'
        dot_str += "}\n"
        # print("vvbn", dot)
        Dag.draw_dot(dot_str, j_embed=jupyter, circo=circo)

    def describe_self(self,  long_desc=True):
        """
        This method prints a description of the Dag self. It writes a long
        description iff long_desc==True

        Parameters
        ----------
        long_desc; bool

        Returns
        -------
        None

        """
        print("title=", self.title)
        print("arrows:")
        print_list(self.arrows)
        if long_desc:
            print("nodes:")
            for node in self.nodes:
                node.describe_self(long_desc)
        else:
            print(f"num of nodes= {len(self.nodes)}")


if __name__ == "__main__":
    def main():
        pt = Point(.4555555, .8999999)
        bridge1 = Bridge(10, pt, 20, pt)
        bridge2 = Bridge(30, pt, 40, pt)
        bridges = [bridge1, bridge2]

        list_name_to_bridges_x = {"rec_x": bridges}
        nd_a = Node("aa",
                    list_name_to_bridges_x)

        list_name_to_bridges_y = {"rec_y": bridges}
        nd_b = Node("bb",
                    list_name_to_bridges_y)

        list_name_to_bridges_z = {"rec_z": bridges}
        nd_c = Node("cc",
                    list_name_to_bridges_z)

        nodes = [nd_a, nd_b, nd_c]

        ar1 = Arrow("aa",
                    "bb",
                    num_acc=5,
                    num_rej=12)
        ar2 = Arrow("bb",
                    "aa",
                    num_acc=1,
                    num_rej=3)
        ar3 = Arrow("aa",
                    "cc",
                    num_acc=9,
                    num_rej=7)

        arrows = [ar1, ar2, ar3]

        dag = Dag(arrows,
                  nodes,
                  title="test_dag")

        dag.describe_self(long_desc=True)

        dag.draw(
            prob_acc_thold= 0.0,
            num_trials_thold= 1,
            jupyter=False,
            circo=True
        )


    main()