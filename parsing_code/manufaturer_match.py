import pandas as pd
import os
from dir_path import base_dirname


def match_nsnno_manufacturer(nsn_number, approved_companies):
    screw_parts = pd.read_excel(os.path.join(base_dirname, 'data', 'input', 'screw.xlsx'), sheet_name=0)

    screw_parts['PNP'] = screw_parts['PNP'].str.replace('-', '')
    available_manf = screw_parts[screw_parts['PNP'] == nsn_number.strip()]

    manf_not_possible = []
    manf_possible = []

    for source_no in range(1, 5):
        manf_possible = manf_possible + available_manf[
            available_manf[f'Source #{source_no} No go'] != 1][f'Source #{source_no}'].dropna().tolist()

        manf_not_possible = manf_not_possible + available_manf[
            available_manf[f'Source #{source_no} No go'] == 1][f'Source #{source_no}'].dropna().tolist()

    manf_possible = list(set(manf_possible))
    manf_not_possible = list(set(manf_not_possible))

    return manf_possible, manf_not_possible
