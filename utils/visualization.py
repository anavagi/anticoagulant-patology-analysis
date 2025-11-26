import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def load_and_info(file_path):
    """
    Cargamos el fichero CSV y mostramos información sobre valores ausentes, únicos, tipo de datos y valores
    """
    df = pd.read_csv(file_path)
    
    info = []
    for col in df.columns:
        data_type = str(df[col].dtype)
        missing = np.sum(pd.isna(df[col]))
        unique = df[col].nunique()
        
        # Obtenemos las categorías para variables categoricas y valores aleatorios en las numéricas
        if data_type == 'object':
            sample = df[col].dropna().unique().tolist()  # Valores únicos para las categóricas
        else:
            sample = df[col].dropna().unique()[:5].tolist()  # Los primeros 5 valores únicos para las numéricas
        
        info.append([col, data_type, missing, unique, sample])
    
    info_df = pd.DataFrame(info)
    info_df.columns = ['Column', 'Dtype', 'Missing', 'Unique', 'Sample values']
    
    # Mostramos las columnas, con información sobre valores ausentes, únicos y tipo de datos
    display(info_df)
    print("\nEl juego de datos contiene {} variables y {} observaciones, de las cuales {} son duplicadas.".format(df.shape[1], df.shape[0], len(df) - df.duplicated().count()))

    # Devolvemos el dataframe para su uso
    return df