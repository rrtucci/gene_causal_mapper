from Point import *
from Bridge import *
from itertools import product
import pandas as pd


class TS_Record:
    def __init__(self, name, times=TIMES):
        self.name = name
        self.times = times
        self.gene_to_points = None

    def check_self(self):
        assert self.gene_to_points
        for g, pts in self.gene_to_points.items():
            assert len(pts) == len(self.times)

    def read_file(self, in_path, g_range=None):
        df = pd.read_csv(in_path, sep='\t', header=None)
        if g_range is None:
            g_range = range(len(df.len))
        else:
            g_range = range(g_range[0], g_range[1])

        for g_num in g_range:
            self.gene_to_points[df.iloc[g_num, 0]] =\
                df.iloc[g_num, 1:9]
        self.check_self()

    @staticmethod
    def get_gene_to_bridges(rec1, rec2):
        assert len(rec1.gene_to_points) == len(rec2.gene_to_points)
        gene_to_bridges = {}
        for g in rec1.gene_to_points.keys():
            if g in rec2.gene_to_points.keys():
                for i1, i2 in product(range(len(rec1.times)),
                                      range(len(rec2.times))):
                    t1 = rec1.times[i1]
                    t2 = rec2.times[i2]
                    pt1 = rec1.gene_to_points[g][i1]
                    pt2 = rec1.gene_to_points[g][i2]
                    if Point.are_sim(pt1, pt2):
                        bridge = Bridge(t1, pt1, t2, pt2)
                        gene_to_bridges.setdefault(g, []).append(bridge)
        return gene_to_bridges