import pandas as pd
import numpy as np
from globals import *


def create_strain_files(in_path, out_dir):
    """
    Reads DREAM3 TSV file and writes a separate TSV file for each of the 4
    strains

    """
    df = pd.read_csv(in_path, sep='\t', header=None)
    for strain_num in range(4):
        out_path = out_dir + "/" + STRAINS[strain_num] + ".tsv"
        start_col = 3 + strain_num * 8
        end_col = start_col + 8
        df1 = df.iloc[:, np.r_[1:2, start_col:end_col]]
        df1 = df1.dropna(subset=[df1.columns[0]])
        if STRAINS[strain_num] == "gat1_d":
            df1 = df1[
                ~df1.apply(lambda row: row.astype(str).str.contains(
                    "PREDICT")).any(axis=1)]
        df1.to_csv(out_path, sep='\t', index=False, header=False)


if __name__ == "__main__":
    create_strain_files(
        "data/DREAM3_GeneExpressionChallenge_ExpressionData_UPDATED.txt",
        "data"
    )
