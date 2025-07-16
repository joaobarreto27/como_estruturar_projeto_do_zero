import pandas as pd
import os
import glob
from pathlib import Path

"""
receber um dataframe e salvar como excel

args: 
    data_frame (pd.DataFrame): dataframe a ser salvo
    output_folder (str): caminho onde o arquivo será salvo
    file_name (str): nome do arquivo a ser salvo

return: Arquivo Excel salvo no caminho especificado
"""

def load_excel(dataframe: pd.DataFrame, output_folder:str, file_name:str) -> str:
    current_dir = Path(__file__).resolve().parents[1]
    path_file = os.path.join(current_dir, output_folder, file_name)

    # Verifica se o diretório de saída existe, se não, cria
    os.makedirs(os.path.dirname(path_file), exist_ok=True)

    dataframe.to_excel(f"{path_file}.xlsx", index=False)
    return "Arquivo salvo com sucesso"