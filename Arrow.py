import copy as cp


class Arrow:
    """
    This class defines an arrow that points from gene `start_g` to gene
    `end_g`. The class also stores the parameters num_acc (number accepted)
    and num_rej ( number rejected).  An arrow is either accepted or rejected
    when comparing two bridges


    Attributes
    ----------
    end_g: str
    num_acc: int
    num_rej: int
    start_g: str

    """

    def __init__(self, start_g, end_g, num_acc=0, num_rej=0):
        """
        Constructor

        Parameters
        ----------
        start_g: str
        end_g: str
        num_acc: int
        num_rej: int
        """

        self.start_g = start_g
        self.end_g = end_g
        self.num_acc = num_acc
        self.num_rej = num_rej

    def __str__(self):
        """
        This magic method returns a string describing an instance of this
        class any time that instance occurs in print()

        Returns
        -------
        str

        """
        return (f"{self.start_g}->{self.end_g}"
                f" (acc, rej)=({self.num_acc}, {self.num_rej})")

    def recognize_ends(self, start_g, end_g):
        """
        This method returns True iff self.start_g = start_g and self.end_g =
        end_g

        Parameters
        ----------
        start_g: str
        end_g: str

        Returns
        -------
        bool

        """
        return self.start_g == start_g and self.end_g == end_g

    @staticmethod
    def same_start_end(ar1, ar2):
        """
        This method returns True iff ar1.start_g = ar2.start_g and ar1.end_g
        = ar2.end_g

        Parameters
        ----------
        ar1: Arrow
        ar2: Arrow

        Returns
        -------
        bool

        """
        return (ar1.start_g == ar2.start_g and
                ar1.end_g == ar2.end_g)

    @staticmethod
    def find_arrow(arrows, start_g, end_g):
        """
        This method tries to find and Arrow from gene `start_g` to gene
        `end_g` within the list `arrows`. If it finds one, it returns it.
        otherwise, it returns None.


        Parameters
        ----------
        arrows: list[Arrow]
        start_g: str
        end_g: str

        Returns
        -------
        Arrow|None

        """
        ar1 = None
        for ar in arrows:
            if ar.start_g == start_g and ar.end_g == end_g:
                ar1 = ar
                break
        return ar1

    def accept(self):
        """
        This method increments `self.num_acc` (number of accepted arrows) by
        one.

        Returns
        -------
        None

        """
        self.num_acc += 1

    def reject(self):
        """
        This method increments `self.num_rej` (number of rejected arrows) by
        one.

        Returns
        -------
        None

        """
        self.num_rej += 1

    def get_num_trials(self):
        """
        This method returns the total number of trials (= self.num_acc +
        self.num_rej)

        Returns
        -------
        int

        """
        return self.num_acc + self.num_rej

    def get_prob_acc(self):
        """
        This method returns the probability of acceptance of the self Arrow.

        Returns
        -------
        float

        """
        return self.num_acc / self.get_num_trials()

    def above_thresholds(self,
                         prob_acc_thold,
                         num_trials_thold):
        """
        thold=threshold. This method returns True iff the `self.prob_acc()`
        exceeds `prob_acc_thold` and `self.get_num_trials()` exceeds
        `num_trials_thold`

        Parameters
        ----------
        prob_acc_thold: float
        num_trials_thold: int

        Returns
        -------
        bool

        """
        if self.get_prob_acc() > prob_acc_thold and \
                self.get_num_trials() > num_trials_thold:
            return True
        else:
            return False

    @staticmethod
    def merge_two_arrows(ar1, ar2):
        """
        This method has two Arrow's ar1 and ar2 as input. It returns a new
        Arrow that merges the two input Arrow's.

        Parameters
        ----------
        ar1: Arrow
        ar2: Arrow

        Returns
        -------
        Arrow

        """
        assert ar1.start_g == ar2.start_g
        assert ar1.end_g == ar2.end_g
        ar = cp.copy(ar1)
        ar.num_acc += ar2.num_acc
        ar.num_rej += ar2.num_rej
        return ar

if __name__ == "__main__":
    def main():
        ar1 = Arrow("start1",
                    "end1",
                    num_acc=5,
                    num_rej=12)
        ar2 = Arrow("start1",
                    "end1",
                    num_acc=1,
                    num_rej=3)
        ar3 = Arrow("start1",
                    "end2",
                    num_acc=2,
                    num_rej=7)
        print(ar1)
        arrows = [ar1, ar2, ar3]
        ar12 = Arrow.merge_two_arrows(ar1, ar2)
        print("merge1,2:\n", ar1, "\n", ar2, "\n", ar12 )
        print("compare ar1, ar2", Arrow.same_start_end(ar1, ar2))
        print("ar1, ar2 same", Arrow.same_start_end(ar1, ar2))
        print("ar1, ar3 same", Arrow.same_start_end(ar1, ar3))
        print(Arrow.find_arrow([ar3, ar1],
                               "start1",
                               "end2"))

    main()