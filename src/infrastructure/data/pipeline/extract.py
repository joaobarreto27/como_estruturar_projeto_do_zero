import os
import glob
import pandas as pd
from typing import List
from pathlib import Path

"""
função para ler os arquivos de uma pasta data/input e retornar uma lista de dataframes

args: input_path (str): caminho da pasta com os arquivos

return: lista de dataframes
"""

def extract_from_excel(folder_name: str, extension_type) -> List[pd.DataFrame]:
    current_dir = Path(__file__).resolve().parents[1]
    path = os.path.join(current_dir,folder_name)

    all_files = glob.glob(os.path.join(path, f"*.{extension_type}"))
    
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel("input", "xlsx")
    print(data_frame_list)