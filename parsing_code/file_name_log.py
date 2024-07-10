import pandas as pd
import os
import shutil


def copy_pdfs(temp_folder, date_folder, log_file):

    existing_pdfs = pd.read_csv(log_file)['filename'].tolist()
    for filename in os.listdir(temp_folder):
        source_pdf_path = os.path.join(temp_folder, filename)
        if ((filename not in ['.ipynb_checkpoints', '.DS_Store']) and (filename not in existing_pdfs)
                and (not filename.endswith(".crdownload"))):
                shutil.copy(source_pdf_path, date_folder)
                existing_pdfs.append(filename)

    pd.DataFrame({'filename': existing_pdfs}).to_csv(log_file, index=False)