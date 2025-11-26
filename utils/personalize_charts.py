import pandas as pd
import numpy as np
# plotting and displaying in the notebook
import seaborn as sns
from matplotlib import pyplot as plt
from IPython.display import display

def display_categorical(feature, df='df_investig_INR', target='INR_Group'):
    """
    Para variables categóricas: pie chart y bar chart
    """
    # Gráficas en una fila con dos columnas, siendo el segundo plot 1,5 veces mas ancho
    fig, axs = plt.subplots(1, 2, figsize=(16,4), gridspec_kw={'width_ratios':[1,1.5]})

    value_counts = df[feature].value_counts()
    colors = ["#2ecc71","#f39c12", "#e74c3c"]

    axs[0].pie(
        value_counts.values,
        labels=value_counts.index,
        explode=([0.05]*len(value_counts.index)),
        autopct='%.2f%%',
        colors=colors
    )

    if feature == target:
        axs[1].barh(
            y=value_counts.index.astype(str),
            width=value_counts.values,
            color=colors[:len(value_counts.index)]
        )
        axs[1].set_xlabel('Data count')
        axs[1].grid(alpha=0.4)
        
        for index, values in enumerate(value_counts):
            axs[1].text(values + 5, index, str(values), va='center')
    
    else:
        # Mostramos la distribución del bar chart por la variable target
        sns.histplot(
            data=df,
            y=feature,
            hue=target,
            multiple="fill",
            shrink=0.8,
            palette=colors,
            ax=axs[1]
        )
        axs[1].set_ylabel(feature)
        axs[1].set_xlabel('Proportion')
        axs[1].grid(alpha=0.4)

    fig.suptitle('Distribución de la variable ' + feature)
    plt.tight_layout(pad=1)


    return plt


def display_numerical(feature,  df='df_investig_INR'):
    """
    Para variables numéricas: histograma, boxplot y tabla descriptiva
    """
    fig, axs = plt.subplots(1, 2, figsize=(16,4), gridspec_kw={'width_ratios':[1.5,1]})

    colors = ["#2ecc71","#f39c12", "#e74c3c"]

    sns.histplot(data=df,
                 x=df[feature],
                 hue=df['INR_Group'],
                 palette=colors,
                 multiple='stack',
                 ax=axs[0])
    axs[0].grid(alpha=0.4)
    
    sns.violinplot(data=df,
               x=df['INR_Group'],
               y=df[feature],
               hue='INR_Group', # Opcional si solo quieres un color por 'x'
               palette=colors,
               ax=axs[1],
               inner='quartile') # Muestra los cuartiles dentro del violín

    if axs[1].legend_ is not None:
        axs[1].legend_.remove()
    
    fig.suptitle(f'INR para la distribución de la variable {feature}')
    plt.tight_layout(pad=1)
    plt.show()

    # Mostramos las estadísticas de la característica agrupada por la variable objetivo
    display(df.groupby('INR_Group')[feature].describe())

    return plt
