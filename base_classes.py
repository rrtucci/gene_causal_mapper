from globals import *
from utils import *

class Point:
    def  __init__(self, x, xdot):
        self.x = x
        self.xdot = xdot

    @staticmethod
    def are_sim(pt1, pt2):
        if (abs(pt1.x-pt2.x) < X_RAD and
                abs(pt1.xdot - pt2.xdot) < XDOT_RAD):
            return True
        else:
            return False

class Arrow:

    def __init__(self, start_g, end_g):
        self.start_g = start_g
        self.end_g = end_g
        self.num_acc = 0
        self.num_rej = 0

    @staticmethod
    def same_start_end(ar1, ar2):
        return (ar1.start_g == ar2.start_g and
                ar1.end_g == ar2.end_g)

    @staticmethod
    def find_arrow(arrows, start_g, end_g):
        ar1 = None
        for ar in arrows:
            if ar.start_g == start_g and ar.end_g == end_g:
                ar1 = ar
                break
        return ar1

    def accept(self):
        self.num_acc += 1

    def reject(self):
        self.reject += 1

    def get_num_trials(self):
        return self.num_acc + self.num_rej

    def get_prob_acc(self):
        return self.num_acc/self.get_num_trials()

    def above_threshold(self, th_prob_acc, th_num_trials):
        if self.get_prob_acc() > th_prob_acc and \
            self.get_num_trials() > th_num_trials:
            return True
        else:
            return False

    @staticmethod
    def merge_two_arrows(ar1, ar2):
        assert ar1.start_g == ar2.start_g
        assert ar1.end_g == ar2.end_g
        ar = cp.copy(ar1)
        ar.num_acc += ar2.num_acc
        ar.num_rej += ar2.num_rej
        return ar


class Bridge:
    def __init__(self, t1, pt1, t2, pt2):
        self.t1 = t1
        self.pt1 = pt1
        self.t2 = t2
        self.pt2 = pt2

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

