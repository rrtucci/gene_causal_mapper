import pandas as pd
import numpy as np
from globals import *


def create_4_strain_files(in_path, out_dir, del_PREDICT=True):
    """
    Reads DREAM3 TSV file and writes a separate TSV file for each of the 4
    strains

    """
    df = pd.read_csv(in_path, sep='\t', header=None)
    for strain_num in range(4):
        out_path = out_dir + "/" + STRAINS[strain_num] + ".csv"
        start_col = 3 + strain_num * 8
        end_col = start_col + 8
        df1 = df.iloc[:, np.r_[1:2, start_col:end_col]]
        df1 = df1.dropna(subset=[df1.columns[0]])
        if STRAINS[strain_num] == "gat1" and del_PREDICT:
            df1 = df1[
                ~df1.apply(lambda row: row.astype(str).str.contains(
                    "PREDICT")).any(axis=1)]
        df1.to_csv(out_path, index=False, header=False)


if __name__ == "__main__":
    create_4_strain_files(
        f"data/{DREAM3_DATASET}",
        "data"
    )
