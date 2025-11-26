import pandas as pd
import re
from typing import Dict, List, Union


# Diccionario de abreviaciones para tus diagnósticos
variable_rename_map = {
    'FLEBITIS I TROMBOFLEBITIS VASOS PROFUNDS NE EXTREM. INF. NE': 'Flebitis_Profunda',
    'FIBRIL·LACIÓ AURICULAR NO ESPECIFICADA': 'FA_NE',
    'ALETEIG [FLUTTER] AURICULAR NO ESPECIFICAT': 'Flutter_NE',
    'TRASTORN NO REUMÀTIC DE LA VÀLVULA AÒRTICA NO ESPECIFICAT': 'Valv_Aort_NReum_NE',
    "ALTRES TIPUS D'EMBÒLIA PULMONAR SENSE COR PULMONAR AGUT": 'EP_Other_No_CorPulm',
    'FIBRIL·LACIÓ AURICULAR PERMANENT': 'FA_Perm',
    'FIBRIL·LACIÓ AURICULAR CRÒNICA': 'FA_Cron',
    'ARRÍTMIA CARDÍACA NO ESPECIFICADA': 'Arritmia_NE',
    "ÚS D'ANTICOAGULANTS A LLARG TERMINI (ACTUAL)": 'Anticoagulant_LT',
    'EMBÒLIA I TROMBOSI DE VENA NO ESPECIFICADA, AGUDES': 'Trombosi_Venosa_Aguda',
    "ALT. TRAST. D'ARTÈRIES ARTERIOLES I CAPIL·LARS EN MAL. CAL": 'Alt_Art_Arter_Cap',
    'MIOCARDIOPATIA DILATADA': 'Miocardiopatia_Dilatada',
    'INFART CEREBRAL NO ESPECIFICAT': 'Infart_Cerebral_NE',
    'ALTRES TIPUS DE DESPOLARITZACIÓ PREMATURA': 'Despol_Prem_Other',
    'ESTENOSI AÒRTICA NO REUMÀTICA (VÀLVULA)': 'Estenosi_Aort_NReum',
    "TRAST. D'ADAPTACIÓ MIXT D'ANSIETAT I ESTAT D'ÀNIM DEPRIMIT": 'Trast_Adapt_Mixt',
    "ATEROSCLEROSI D'ARTÈRIES NADIUES NE, EXTREMITAT NE": 'Aterosclerosis_NE',
    'ATAC ISQUÈMIC CEREBRAL TRANSITORI NO ESPECIFICAT': 'AIT_NE',
    'TRASTORN NO REUMÀTIC DE LA VÀLVULA MITRAL NO ESPECIFICAT': 'Valv_Mitral_NReum_NE',
    'SÍNCOPE I COL·LAPSE': 'Sincop',
    'HEMORRÀGIA SUBDURAL NO TRAUMÀTICA NO ESPECIFICADA': 'HSD_NE',
    'PALPITACIONS': 'Palpitacions',
    'TAQUICÀRDIA PAROXISMAL NO ESPECIFICADA': 'Taquicardia_Parox_NE',
    'CARDIOPATIA ISQUÈMICA CRÒNICA NO ESPECIFICADA': 'CI_Cron_NE',
    'VALVULOPATIA MITRAL REUMÀTICA NO ESPECIFICADA': 'Valv_Mitral_Reum_NE',
    'IMEST DE LOCALITZACIÓ NO ESPECIFICADA': 'IMEST_NE',
    'PRESÈNCIA DE VÀLVULA CARDÍACA PROTÈTICA': 'Valvula_Protetica',
    'INSUFICIÈNCIA MITRAL NO REUMÀTICA (VÀLVULA)': 'Insuf_Mitral_NReum',
    'FIBRIL·LACIÓ AURICULAR PAROXISMAL': 'FA_Parox',
    'ANGINA DE PIT NO ESPECIFICADA': 'Angina_NE',
    'VASCULOPATIA NECROSANT NO ESPECIFICADA': 'Vasculopatia_Nec_NE',
    'LUPUS ERITEMATÓS SISTÈMIC NO ESPECIFICAT': 'LES_NE',
    'BONY EN MAMA NO ESPECIFICAT, MAMA NO ESPECIFICADA': 'Bony_Mama_NE',
    'INSUFICIÈNCIA AÒRTICA NO REUMÀTICA (VÀLVULA)': 'Insuf_Aort_NReum',
    "TRASTORN VASCULAR NO ESPECIFICAT D'INTESTÍ": 'Trast_Vascular_Intesti_NE',
    'ENDOCARDITIS I TRASTORNS VÀLVULA CARDÍACA EN MAL. CAL': 'Endocarditis_Cal',
    "ALTRES TIPUS D'HEMOGLOBINOPATIA": 'Hemoglobinopatia_Other',
    'ANGIOPATIA PERIFÈRICA NO ESPECIFICADA': 'Angiopatia_Periferica_NE',
    'INSUFICIÈNCIA CARDÍACA NO ESPECIFICADA': 'IC_NE',
    'INSUFICIÈNCIA MITRAL REUMÀTICA': 'Insuf_Mitral_Reum',
    'CIRROSI HEPÀTICA ALCOHÒLICA, SENSE ASCITES': 'Cirrosi_Alcoholica_NoAsc',
    'SÍNDROME POSTTROMBÒTICA SENSE COMPLICACIONS, EXTREMITAT NE': 'SPT_NoComp_NE',
    'FIBRIL·LACIÓ AURICULAR CRÒNICA NE': 'FA_Cron_NE',
    'FLEBITIS I TROMBOFLEBITIS DE LOCALITZACIÓ NO ESPECIFICADA': 'Flebitis_NE'
}

def shorten_diagnoses(df: pd.DataFrame, 
                           column: str = 'DESCRIPTION',
                           inplace: bool = False,
                           custom_map: Dict[str, str] = None) -> pd.DataFrame:
    """
    Replace long medical variable names with shorter, descriptive ones.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with long variable names
    column : str
        Column name containing the variable descriptions (default: 'DESCRIPTION')
    inplace : bool
        If True, modify the column in place. If False, create a new column (default: False)
    custom_map : Dict[str, str]
        Additional custom mappings to merge with default mappings
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with shortened variable names
    """
    if not inplace:
        df = df.copy()
    
    # Merge custom mappings if provided
    rename_map = variable_rename_map.copy()
    if custom_map:
        rename_map.update(custom_map)
    
    # Apply mapping
    if inplace:
        df[column] = df[column].map(rename_map).fillna(df[column])
    else:
        df[f'{column}'] = df[column].map(rename_map).fillna(df[column])
    
    mapped_count = df[column].isin(rename_map.keys()).sum()
    total_count = len(df)
    print(f"Shortened {mapped_count}/{total_count} variable names ({mapped_count/total_count*100:.1f}%)")
    
    return df
