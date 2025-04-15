import copy as cp


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
        return self.num_acc / self.get_num_trials()

    def above_thresholds(self,
                         prob_acc_thold,
                         num_trials_thold):
        if self.get_prob_acc() > prob_acc_thold and \
                self.get_num_trials() > num_trials_thold:
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
