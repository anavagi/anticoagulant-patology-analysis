import pandas as pd
import numpy as np

def create_inr_group(data_series):
    """Crea la columna categórica INR_Group a partir de una serie de datos INR."""
    target_col = 'INR'
    
    # Se ajustan los bins para que el rango Normal sea [2.0, 3.0]
    # Usamos 3.0 + 1e-6 para incluir 3.0 en el rango Normal cuando right=False (intervalo abierto a la derecha)
    min_val = data_series.min() if not data_series.empty else -1
    max_val = data_series.max() if not data_series.empty else 4
    
    # Aseguramos que los bins cubran el rango de los datos si es necesario, 
    # aunque los límites principales son fijos
    bins = [min(min_val - 1, 0), 2.0, 3.0 + 1e-6, max(max_val + 1, 5)]
    
    labels = ['Bajo (<2.0)', 'Normal (2.0-3.0)', 'Alto (>3.0)']
    
    # Filtramos la serie para eliminar posibles NaNs si es necesario antes de agrupar
    data_series = data_series.dropna()
    
    if data_series.empty:
        return pd.Series([], dtype='category')
        
    return pd.cut(
        data_series, 
        bins=bins, 
        labels=labels, 
        right=False, # El intervalo es [a, b)
        include_lowest=True
    ).astype('category')