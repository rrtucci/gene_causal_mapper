from turtledemo.penrose import start
from Dag import *
from TS_Record import *
import copy as cp

class DagAtlas:
    def __init__(self, cum_dag):
        self.cum_dag = cum_dag

    @staticmethod
    def extract_dag_from_two_recs(rec1, rec2):
        dag = Dag()
        gene_to_bridges = TS_Record.get_gene_to_bridges(rec1, rec2)
        genes = gene_to_bridges.keys()
        for gene_a, gene_b in product(genes, genes):
            if gene_a != gene_b:
                bridge_a = gene_to_bridges[gene_a]
                bridge_b = gene_to_bridges[gene_b]
                ta1, ta2 = bridge_a.t1, bridge_a.t2
                tb1, tb2 = bridge_b.t1, bridge_b.t2
                if ta1 < tb1 and ta2 < tb2:
                    accept = True
                    start_g, end_g = gene_a, gene_b
                    acc_bridge_a = bridge_a
                    acc_bridge_b = bridge_b
                elif ta1 > tb1 and ta2 > tb2:
                    accept = True
                    start_g, end_g = gene_b, gene_a
                    acc_bridge_a = bridge_a
                    acc_bridge_b = bridge_b
                elif ta1 < tb1 and ta2 > tb2:
                    accept = False
                    start_g, end_g = gene_a, gene_b
                    acc_bridge_a = None
                    acc_bridge_b = None
                elif ta1 > tb1 and ta2 < tb2:
                    accept = False
                    start_g, end_g = gene_b, gene_a
                    acc_bridge_a = None
                    acc_bridge_b = None
                else:
                    assert False
                dag.update_arrow(start_g, end_g, accept)
                dag.update_node(gene_a, rec1, rec2, acc_bridge_a)
                dag.update_node(gene_b, rec1, rec2, acc_bridge_b)
        return dag

    @staticmethod
    def merge_two_dags_into_one(dag1, dag2):
        dag = cp.deepcopy(dag1)
        for node2 in dag2.nodes:
            nd = dag.node_with_this_gene(node2.gene)
            if nd:
                nd = Node.merge_two_nodes(nd, node2)
            else:
                dag.nodes.append(cp.deepcopy(node2))

        for ar2 in dag2.arrows:
            ar = Arrow.find_arrow(dag.arrows,
                                  ar2.start_g,
                                  ar2.end_g)
            if ar:
                ar = Arrow.merge_two_arrows(ar, ar2)
            else:
                dag.arrows.append(ar2)
        return dag