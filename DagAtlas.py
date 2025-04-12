from base_classes import *
from Dag import *
from TS_Record import *

class DagAtlas:
    def __init__(self, cum_dag):
        self.cum_dag = cum_dag

    @staticmethod
    def get_dag_from_two_recs(rec1, rec2):
        dag = Dag()
        TS_Record.get_gene_to_bridges(rec1, rec2)

