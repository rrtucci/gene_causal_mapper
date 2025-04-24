from Point import *
from utils import *
from Bridge import *
from itertools import product
import pandas as pd


class TS_Record:
    """
    The main purpose of this class is to read a csv file that we call a
    "time-series (TS) record" and to create the dictionary
    `gene_to_bridges` that maps each gene name to a list of Bridge's.

    Attributes
    ----------
    gene_to_points: dict[str, list[Point]]
        dictionary that maps each gene name to a list of Point's
    name: str
        name of TS_Record
    times: list[int]
        a Point contains x and xdot. `times` is a list of times such as
        the 8 times in TIMES. `self.gene_to_points[gene]` is a list of
        Point's of the same length as the list `times`. Together,
        these two lists specify a trajectory (t, x, xdot) in phase space.

    """

    def __init__(self,
                 name,
                 in_path,
                 times=TIMES,
                 num_genes=None):
        """
        Constructor

        Parameters
        ----------
        name: str
            name of TS record.
        in_path: str
            input path for csv
        times: list[int]
        num_genes: int
            if the number of genes in file `in_path` is greater than num_genes,
            only first `num_genes` genes (rows) of the file are read.
        """
        self.name = name
        self.times = times
        self.gene_to_points = {}
        self.read_file(in_path, num_genes=num_genes)

    def check_self(self):
        """
        Do some checks. Especially, check that the two lists `self.times`
        and `self.gene_to_points[gene]` have the same length, for all gene's.

        Returns
        -------
        None

        """
        assert self.gene_to_points
        for g, pts in self.gene_to_points.items():
            assert len(pts) == len(self.times), \
                f"{len(pts)}!={len(self.times)}"

    def read_file(self, in_path, num_genes=None):
        """
        This method reads the file at `in_path` and fills the dictionary
        `self.gene_to_points`.

        Parameters
        ----------
        in_path: str
        num_genes: int

        Returns
        -------
        None

        """
        df = pd.read_csv(in_path)
        if num_genes is None or num_genes > df.shape[0]:
            num_genes = df.shape[0]
        for g_num in range(num_genes):
            gene = df.iloc[g_num, 0]
            self.gene_to_points[gene] = []
            for t in range(len(self.times)):
                col = t + 1
                x = df.iloc[g_num, col]
                if t == 0:
                    xdot = 0.0
                else:
                    delta_t = self.times[t] - self.times[t - 1]
                    xdot = (x - df.iloc[g_num, col - 1]) / delta_t
                self.gene_to_points[gene].append(Point(x, xdot))
            # for xdot of first point, use xdot of second point
            self.gene_to_points[gene][0].xdot = \
                self.gene_to_points[gene][1].xdot

        self.check_self()

    @staticmethod
    def get_gene_to_bridges(rec1,
                            rec2,
                            verbose=True,
                            more_verbose=True):
        """
        This method is given as input two TS_Record's `rec1` and `rec2`.
        It returns the dictionary `gene_to_bridges` which maps each gene
        name to a lists of Bridge's.

        Parameters
        ----------
        rec1: TS_Record
        rec2: TS_Record
        verbose: bool
        more_verbose: bool

        Returns
        -------
        gene_to_bridges: dict[str, list[Bridge]]

        """
        print("Entering TS_Record.get_gene_to_bridges() "
              f"for rec1={rec1.name}, rec2={rec2.name}")
        gene_to_bridges = {}
        for g in rec1.gene_to_points:
            if g in rec2.gene_to_points:
                for i1, i2 in product(range(len(rec1.times)),
                                      range(len(rec2.times))):
                    t1 = rec1.times[i1]
                    pt1 = rec1.gene_to_points[g][i1]
                    t2 = rec2.times[i2]
                    pt2 = rec2.gene_to_points[g][i2]
                    if Point.are_sim(pt1, pt2):
                        bridge = Bridge(t1, pt1, t2, pt2)
                        gene_to_bridges.setdefault(g, []).append(bridge)
        print("Exiting TS_Record.get_gene_to_bridges()")
        if verbose:
            print("gene to num of bridges=")
            print({gene: len(gene_to_bridges[gene]) for gene in
                   gene_to_bridges})
            if more_verbose:
                for gene in gene_to_bridges:
                    print(gene)
                    print("t1(x1, xdot1)----t2(x2, xdot2)")
                    print_list(gene_to_bridges[gene])
        return gene_to_bridges

    def describe_self(self):
        print(self.name, self.times)
        print_dict(self.gene_to_points)


if __name__ == "__main__":
    def main1():
        rec1 = TS_Record("gat1",
                         "data/gat1.csv",
                         num_genes=5
                         )
        rec1.describe_self()


    def main2():
        rec1 = TS_Record("gat1",
                         "data/gat1.csv",
                         num_genes=10
                         )
        rec2 = TS_Record("gcn4",
                         "data/gcn4.csv",
                         num_genes=10
                         )
        gene_to_bridges = \
            TS_Record.get_gene_to_bridges(rec1,
                                          rec2,
                                          verbose= True,
                                          more_verbose=True)
        print_dict(gene_to_bridges)


    main1()
    main2()
