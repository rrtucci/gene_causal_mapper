import pandas as pd
from globals import *


def create_strain_files(in_path, out_dir):
    """
    Reads DREAM3 TSV file and writes a separate TSV file for each of the 4
    strains

    """
    df = pd.read_csv(in_path, sep='\t', header=None)
    for strain_num in range(len(STRAINS)):
        out_path = out_dir + "/" + STRAINS[strain_num] + ".tsv"
        start_col = 3 + strain_num*8
        end_col = start_col + 8
        df_selected = df.iloc[:, start_col:end_col]
        df_filtered = df_selected[df_selected.iloc[:, 1] != "NaN"]
        df_filtered.to_csv(out_path, sep='\t', index=False, header=False)