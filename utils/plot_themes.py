import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from utils.constants import *

def distribution_INRGrout_Train(datasets):
    # Convertir cada serie de 'INR' a su respectivo 'INR_Group'
    grouped_datasets = [create_inr_group(ds) for ds in datasets]

    titles = ["Dataset", "Train full", "Test full", "Train", "Validation", "Calibration", "Test"]

    # --- Generación de los gráficos de pastel ---

    # Definir colores para las categorías (consistentes en todos los gráficos)
    # Asegúrate de que el orden sea 'Bajo', 'Normal', 'Alto'
    category_colors = {
        'Bajo (<2.0)': '#ADD8E6',   # Azul claro
        'Normal (2.0-3.0)': '#90EE90', # Verde claro
        'Alto (>3.0)': '#FFB6C1'      # Rosa claro
    }
    # Obtener las etiquetas en el orden deseado
    category_labels = ['Bajo (<2.0)', 'Normal (2.0-3.0)', 'Alto (>3.0)']
    color_list = [category_colors[label] for label in category_labels]

    fig, axs = plt.subplots(1, 7, figsize=(20, 5)) # Ajuste de tamaño para mejor visualización

    for i in range(len(grouped_datasets)):
        # Contar la ocurrencia de cada grupo categórico
        # Usar .value_counts() con .reindex() para asegurar que todas las categorías 
        # y el orden sean consistentes, incluso si una categoría no tiene datos.
        class_counts = grouped_datasets[i].value_counts().reindex(category_labels, fill_value=0)
        
        # Filtrar las categorías con conteo > 0 para el plot
        counts_to_plot = class_counts[class_counts > 0]
        labels_to_plot = counts_to_plot.index.tolist()
        colors_to_plot = [category_colors[label] for label in labels_to_plot]
        
        ax = axs[i]
        
        # Solo graficar si hay datos
        if not counts_to_plot.empty:
            wedges, _, autotexts = ax.pie(
                counts_to_plot, 
                labels=labels_to_plot, 
                autopct='%1.1f%%', 
                startangle=140, 
                colors=colors_to_plot,
                textprops={'fontsize': 9} # Tamaño de fuente de la etiqueta para mejor ajuste
            )
            
            # Añadimos número de ejemplos junto con el porcentaje por clase
            for autotext, count in zip(autotexts, counts_to_plot):
                autotext.set_text(f"{autotext.get_text()}\n({count})")
                autotext.set_fontsize(8) # Tamaño de fuente del porcentaje/conteo
        else:
            # Mostrar un mensaje si el subconjunto está vacío
            ax.text(0.5, 0.5, 'Sin Datos', ha='center', va='center', fontsize=12)

        ax.set_title(titles[i] + " (N=" + str(len(datasets[i])) + ")", fontsize=10)
        ax.axis("equal")

    plt.suptitle("Distribución de la Variable INR_Group por Subconjunto de Datos", fontsize=14, y=1.02)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajuste para el supertítulo
    plt.show()
        