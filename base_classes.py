from globals import *

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

    def recognize_end_gs(self, start_g, end_g):
        if start_g == self.start_g and end_g == self.end_g:
            return True
        else:
            return False

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

class Bridge:
    def __init__(self, t1, pt1, t2, pt2):
        self.t1 = t1
        self.pt1 = pt1
        self.t2 = t2
        self.pt2 = pt2

class Node:
    def __init__(self, gene):
        self.gene = gene
        self.rec_pair_to_acc_bridge = {}

