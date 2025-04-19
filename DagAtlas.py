from turtledemo.penrose import start
from Dag import *
from TS_Record import *
import copy as cp


class DagAtlas:

    @staticmethod
    def extract_dag_from_two_recs(rec_name1,
                                  rec_name2,
                                  num_genes=None):
        """

        Parameters
        ----------
        rec_name1: str
        rec_name2: str
        num_genes: int

        Returns
        -------
        Dag

        """
        rec1_path = f"data/{rec_name1}.csv"
        rec2_path = f"data/{rec_name2}.csv"
        rec1 = TS_Record(rec_name1,
                         rec1_path,
                         num_genes=num_genes)
        rec2 = TS_Record(rec_name2,
                         rec2_path,
                         num_genes=num_genes)

        dag = Dag()
        gene_to_bridges = TS_Record.get_gene_to_bridges(rec1, rec2)
        genes = list(gene_to_bridges.keys())
        rg = range(len(genes))
        list_name = f"{rec1.name}&{rec2.name}"
        for a, b in product(rg, rg):
            if a < b:
                bridges_a = gene_to_bridges[genes[a]]
                bridges_b = gene_to_bridges[genes[b]]
                for bridge_a, bridge_b in product(bridges_a, bridges_b):
                    t1a, t2a = bridge_a.t1, bridge_a.t2
                    t1b, t2b = bridge_b.t1, bridge_b.t2
                    if t1a < t1b and t2a < t2b:
                        accept = True
                        start_g, end_g = genes[a], genes[b]
                        acc_bridge_a = bridge_a
                        acc_bridge_b = bridge_b
                    elif t1a > t1b and t2a > t2b:
                        accept = True
                        start_g, end_g = genes[b], genes[a]
                        acc_bridge_a = bridge_a
                        acc_bridge_b = bridge_b
                    elif (t1a < t1b and t2a > t2b) or \
                            (t1a > t1b and t2a < t2b)  or\
                            (t1a==t1b or t2a==t2b):
                        accept = False
                        start_g, end_g = genes[a], genes[b]
                        acc_bridge_a = None
                        acc_bridge_b = None
                    else:
                        assert False
                    dag.update_arrow(start_g, end_g, accept)
                    dag.update_node(genes[a], list_name, acc_bridge_a)
                    dag.update_node(genes[b], list_name, acc_bridge_b)
        return dag

    @staticmethod
    def merge_two_dags_into_one(dag1, dag2):
        """

        Parameters
        ----------
        dag1: Dag
        dag2: Dag

        Returns
        -------
        Dag

        """
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
    def extract_dag_from_n_recs_mem1(rec_names,
                                     title,
                                     num_genes=None):
        """

        Parameters
        ----------
        rec_names: list[str]
        title: str
        num_genes: int

        Returns
        -------
        Dag

        """
        num_recs = len(rec_names)
        dags = []
        for i in range(1, num_recs):
            dag = DagAtlas.extract_dag_from_two_recs(rec_names[i - 1],
                                                     rec_names[i],
                                                     num_genes)
            dags.append(dag)
        for j in range(1, num_recs-1):
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
        num_genes = 20
        dag = DagAtlas.extract_dag_from_n_recs_mem1(STRAINS,
                                                    title,
                                                    num_genes)

        dag.save_self("data")
        dag1 = Dag(in_path_of_pkl=f"data/{title}.pkl")
        dag1.draw(prob_acc_thold=0.95,
                  num_trials_thold=50,
                  jupyter=False)

    main()