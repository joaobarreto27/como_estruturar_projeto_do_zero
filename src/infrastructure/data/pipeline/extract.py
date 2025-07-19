import glob
import os
from pathlib import Path
from typing import List

import pandas as pd


def extract_from_excel(folder_name: str, extension_type: str) -> List[pd.DataFrame]:
    """
    função para ler os arquivos de uma pasta data/input e retornar uma lista de dataframes

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """

    current_dir = Path(__file__).resolve().parents[1]
    path_file = os.path.join(current_dir, folder_name)

    all_files = glob.glob(os.path.join(path_file, f"*.{extension_type}"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    print(
        "Processo ETL concluído com sucesso! Todos os arquivos foram lidos e convertidos em DataFrames."
    )

    return data_frame_list
