from typing import List

import pandas as pd


def contact_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    função para transformar uma lista de dataframes em um único dataframe
    Esta função concatena uma lista de dataframes em um único dataframe, ignorando os índices originais.
    Ela é útil quando se tem múltiplos dataframes que precisam ser combinados em um único
    args: dataframe para análise ou processamento posterior.
    return: pd.DataFrame
    """

    return pd.concat(data_frame_list, ignore_index=True)
