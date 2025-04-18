from turtledemo.penrose import start
from Dag import *
from TS_Record import *
import copy as cp


class DagAtlas:

    @staticmethod
    def extract_dag_from_two_recs(rec_name1, rec_name2, num_genes=None):
        rec1 = TS_Record(rec_name1)
        rec2 = TS_Record(rec_name2)

        rec1.read_file(f"data//{rec_name1}.tsv")
        rec2.read_file(f"data//{rec_name2}.tsv")

        dag = Dag()
        gene_to_bridges = TS_Record.get_gene_to_bridges(rec1,
                                                        rec2,
                                                        num_genes)
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
                list_name = f"{rec1.name}&{rec2.name}"
                dag.update_node(gene_a, list_name, acc_bridge_a)
                dag.update_node(gene_b, list_name, acc_bridge_b)
        return dag

    @staticmethod
    def merge_two_dags_into_one(dag1, dag2):
        dag = cp.deepcopy(dag1)
        for node2 in dag2.nodes:
            nd = Node.node_with_this_gene(dag.nodes,
                                          node2.gene)
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

    @staticmethod
    def extract_dag_from_n_recs_mem1(rec_names, title, num_genes=None):
        num_recs = len(rec_names)
        dags = []
        for i in range(1, num_recs):
            dag = DagAtlas.extract_dag_from_two_recs(rec_names[i - 1],
                                                     rec_names[i],
                                                     num_genes)
            dags.append(dag)
        for j in range(1, num_recs - 2):
            new_dags = []
            for i in range(1, num_recs - j):
                dag = DagAtlas.merge_two_dags_into_one(dags[i - 1],
                                                       dags[i])
                new_dags.append(dag)
            dags, new_dags = new_dags, dags
            dag = dags[0]
            dag.title = title
        return dag


if __name__ == "__main__":
    def main():
        title = "tempo_dag"
        num_genes = 100
        dag = DagAtlas.extract_dag_from_n_recs_mem1(STRAINS,
                                                    title,
                                                    num_genes)
        dag.save_self("data")
        dag1 = Dag(pkl_in_path=f"data//{title}.pkl")
        dag1.draw(prob_acc_thold=.5,
                  num_trials_thold=10,
                  jupyter=False)
