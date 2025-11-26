import pandas as pd
import re
from typing import Dict, List, Union

# Comprehensive mapping of long variable names to short, descriptive names
variable_rename_map = {
    # Vitals
    'Body Height': 'Height',
    'Body Weight': 'Weight',
    'Body temperature': 'Temperature',
    'Body Temperature': 'Temperature',
    'Body mass index (BMI) [Ratio]': 'BMI',
    'Body mass index (BMI) [Percentile] Per age and sex': 'BMI_Percentile',
    'Heart rate': 'Heart_Rate',
    'Respiratory rate': 'Respiratory_Rate',
    'Systolic Blood Pressure': 'SBP',
    'Diastolic Blood Pressure': 'DBP',
    'Mean blood pressure': 'Mean_BP',
    'Oxygen saturation in Arterial blood': 'O2_Saturation',
    'Capillary refill [Time] of Nail bed': 'Capillary_Refill',
    'Left eye Intraocular pressure': 'IOP_Left',
    'Right eye Intraocular pressure': 'IOP_Right',
    
    # Hematology - Complete Blood Count
    'Leukocytes [#/volume] in Blood by Automated count': 'WBC',
    'Leukocytes [#/volume] in Blood': 'WBC',
    'Erythrocytes [#/volume] in Blood by Automated count': 'RBC',
    'Erythrocytes [#/volume] in Blood': 'RBC',
    'Hemoglobin [Mass/volume] in Blood': 'Hemoglobin',
    'Hemoglobin': 'Hemoglobin',
    'Hematocrit [Volume Fraction] of Blood by Automated count': 'Hematocrit',
    'Hematocrit [Volume Fraction] of Blood': 'Hematocrit',
    'Hematocrit': 'Hematocrit',
    'Platelets [#/volume] in Blood by Automated count': 'Platelets',
    'Platelet Count': 'Platelets',
    'MCV [Entitic volume] by Automated count': 'MCV',
    'MCV': 'MCV',
    'MCH [Entitic mass] by Automated count': 'MCH',
    'MCHC [Mass/volume] by Automated count': 'MCHC',
    'Erythrocyte distribution width [Entitic volume] by Automated count': 'RDW',
    'Erythrocyte distribution width [Ratio] by Automated count': 'RDW_Ratio',
    'RBC Distribution Width': 'RDW',
    'Platelet distribution width [Entitic volume] in Blood by Automated count': 'PDW',
    'Platelet mean volume [Entitic volume] in Blood by Automated count': 'MPV',
    
    # Differential
    'Neutrophils [#/volume] in Blood by Automated count': 'Neutrophils_Abs',
    'Lymphocytes [#/volume] in Blood by Automated count': 'Lymphocytes_Abs',
    'Monocytes [#/volume] in Blood by Automated count': 'Monocytes_Abs',
    'Eosinophils [#/volume] in Blood by Automated count': 'Eosinophils_Abs',
    'Basophils [#/volume] in Blood by Automated count': 'Basophils_Abs',
    'Neutrophils/100 leukocytes in Blood by Automated count': 'Neutrophils_Pct',
    'Lymphocytes/100 leukocytes in Blood by Automated count': 'Lymphocytes_Pct',
    'Monocytes/100 leukocytes in Blood by Automated count': 'Monocytes_Pct',
    'Eosinophils/100 leukocytes in Blood by Automated count': 'Eosinophils_Pct',
    'Basophils/100 leukocytes in Blood by Automated count': 'Basophils_Pct',
    
    # Chemistry - Basic Metabolic Panel
    'Glucose [Mass/volume] in Blood': 'Glucose',
    'Glucose [Mass/volume] in Serum or Plasma': 'Glucose',
    'Glucose': 'Glucose',
    'Urea nitrogen [Mass/volume] in Blood': 'BUN',
    'Urea nitrogen [Mass/volume] in Serum or Plasma': 'BUN',
    'Urea Nitrogen': 'BUN',
    'Creatinine [Mass/volume] in Blood': 'Creatinine',
    'Creatinine [Mass/volume] in Serum or Plasma': 'Creatinine',
    'Creatinine': 'Creatinine',
    'Calcium [Mass/volume] in Blood': 'Calcium',
    'Calcium [Mass/volume] in Serum or Plasma': 'Calcium',
    'Calcium': 'Calcium',
    'Sodium [Moles/volume] in Blood': 'Sodium',
    'Sodium [Moles/volume] in Serum or Plasma': 'Sodium',
    'Sodium': 'Sodium',
    'Potassium [Moles/volume] in Blood': 'Potassium',
    'Potassium [Moles/volume] in Serum or Plasma': 'Potassium',
    'Potassium': 'Potassium',
    'Chloride [Moles/volume] in Blood': 'Chloride',
    'Chloride [Moles/volume] in Serum or Plasma': 'Chloride',
    'Chloride': 'Chloride',
    'Carbon dioxide  total [Moles/volume] in Blood': 'CO2',
    'Carbon dioxide  total [Moles/volume] in Serum or Plasma': 'CO2',
    'Carbon dioxide  total [Moles/volume] in Venous blood': 'CO2_Venous',
    'Carbon Dioxide': 'CO2',
    'Magnesium [Mass/volume] in Serum or Plasma': 'Magnesium',
    'Magnesium [Mass/volume] in Blood': 'Magnesium',
    'Phosphate [Mass/volume] in Serum or Plasma': 'Phosphate',
    'Anion Gap': 'Anion_Gap',
    
    # Chemistry - Liver Function
    'Protein [Mass/volume] in Serum or Plasma': 'Protein',
    'Protein': 'Protein',
    'Albumin [Mass/volume] in Serum or Plasma': 'Albumin',
    'Albumin': 'Albumin',
    'Globulin [Mass/volume] in Serum by calculation': 'Globulin',
    'Globulin': 'Globulin',
    'Bilirubin.total [Mass/volume] in Serum or Plasma': 'Bilirubin_Total',
    'Total Bilirubin (Elevated)': 'Bilirubin_Elevated',
    'Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma': 'ALP',
    'Alkaline Phosphatase': 'ALP',
    'Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma': 'ALT',
    'ALT (Elevated)': 'ALT_Elevated',
    'Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma': 'AST',
    'AST (Elevated)': 'AST_Elevated',
    
    # Chemistry - Lipid Panel
    'Cholesterol [Mass/volume] in Serum or Plasma': 'Cholesterol_Total',
    'Triglycerides': 'Triglycerides',
    'Low Density Lipoprotein Cholesterol': 'LDL',
    'Cholesterol in HDL [Mass/volume] in Serum or Plasma': 'HDL',
    
    # Chemistry - Other
    'Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum or Plasma by Creatinine-based formula (MDRD)': 'eGFR',
    'Glomerular filtration rate/1.73 sq M.predicted': 'eGFR',
    'Iron [Mass/volume] in Serum or Plasma': 'Iron',
    'Iron binding capacity [Mass/volume] in Serum or Plasma': 'TIBC',
    'Iron saturation [Mass Fraction] in Serum or Plasma': 'Iron_Saturation',
    'Ferritin [Mass/volume] in Serum or Plasma': 'Ferritin',
    'Lactate [Moles/volume] in Blood': 'Lactate',
    'Lactate dehydrogenase [Enzymatic activity/volume] in Serum or Plasma by Lactate to pyruvate reaction': 'LDH',
    'Creatine kinase [Enzymatic activity/volume] in Serum or Plasma': 'CK',
    'C reactive protein [Mass/volume] in Serum or Plasma': 'CRP',
    'Procalcitonin [Mass/volume] in Serum or Plasma': 'Procalcitonin',
    'Interleukin 6 [Mass/volume] in Serum or Plasma': 'IL6',
    
    # Cardiac Biomarkers
    'Troponin I.cardiac [Mass/volume] in Serum or Plasma by High sensitivity method': 'Troponin_I',
    'NT-proBNP': 'NT_proBNP',
    'Natriuretic peptide.B prohormone N-Terminal [Mass/volume] in Blood by Immunoassay': 'NT_proBNP',
    
    # Coagulation
    'Prothrombin time (PT)': 'PT',
    'INR in Platelet poor plasma by Coagulation assay': 'INR',
    'aPTT in Blood by Coagulation assay': 'aPTT',
    'Activated clotting time (ACT) of Blood by Coagulation assay': 'ACT',
    'Fibrin D-dimer FEU [Mass/volume] in Platelet poor plasma': 'D_Dimer',
    
    # Arterial Blood Gas
    'pH of Arterial blood': 'pH_Arterial',
    'Carbon dioxide [Partial pressure] in Arterial blood': 'pCO2_Arterial',
    'Oxygen [Partial pressure] in Arterial blood': 'pO2_Arterial',
    'Bicarbonate [Moles/volume] in Arterial blood': 'HCO3_Arterial',
    
    # Venous Blood Gas
    'pH of Venous blood': 'pH_Venous',
    'Carbon dioxide [Partial pressure] in Venous blood': 'pCO2_Venous',
    'Oxygen [Partial pressure] in Venous blood': 'pO2_Venous',
    'Bicarbonate [Moles/volume] in Venous blood': 'HCO3_Venous',
    
    # Endocrine
    'Hemoglobin A1c/Hemoglobin.total in Blood': 'HbA1c',
    'Thyroxine (T4) free [Mass/volume] in Serum or Plasma': 'Free_T4',
    'Thyrotropin [Units/volume] in Serum or Plasma': 'TSH',
    
    # Cardiology
    'Left ventricular Ejection fraction': 'LVEF',
    'Functional capacity NYHA': 'NYHA_Functional',
    'Objective assessment of cardiovascular disease NYHA': 'NYHA_Objective',
    'FEV1/FVC': 'FEV1_FVC_Ratio',
    'Exercise stress test study': 'Stress_Test',
    'Oxygen/Total gas setting [Volume Fraction] Ventilator': 'FiO2',
    
    # Mental Health Scores
    'Patient Health Questionnaire-9: Modified for Teens total score [Reported.PHQ.Teen]': 'PHQ9_Teen',
    'Patient Health Questionnaire 9 item (PHQ-9) total score [Reported]': 'PHQ9',
    'Patient Health Questionnaire 2 item (PHQ-2) total score [Reported]': 'PHQ2',
    'Generalized anxiety disorder 7 item (GAD-7) total score [Reported.PHQ]': 'GAD7',
    'Total score [DAST-10]': 'DAST10',
    'Total score [AUDIT-C]': 'AUDIT_C',
    'Total score [HARK]': 'HARK',
    'Total score [MMSE]': 'MMSE',
    'PROMIS-10 Global Mental Health (GMH) score': 'PROMIS_Mental',
    'PROMIS-10 Global Physical Health (GPH) score': 'PROMIS_Physical',
    
    # Quality of Life - VR-12
    'VR-12 Physical functioning (PF) score - oblique method': 'VR12_Physical_Function',
    'VR-12 Role physical (RP) score - oblique method': 'VR12_Role_Physical',
    'VR-12 Bodily pain (BP) score - oblique method': 'VR12_Pain',
    'VR-12 General health (GH) score - oblique method': 'VR12_General_Health',
    'VR-12 Vitality (VT) score - oblique method': 'VR12_Vitality',
    'VR-12 Social functioning (SF) score - oblique method': 'VR12_Social',
    'VR-12 Role emotion (RE) score - oblique method': 'VR12_Role_Emotion',
    'VR-12 Mental health (MH) score - oblique method': 'VR12_Mental_Health',
    
    # Immunology
    'CD3+CD4+ (T4 helper) cells [#/volume] in Blood': 'CD4_Count',
    
    # Social/Behavioral
    'Tobacco smoking status': 'Smoking_Status',
    'Stress level': 'Stress_Level',
    
    # Physical Exam
    'Physical findings of Abdomen by Palpation': 'Abdominal_Exam',
}


med_map = {
    'heparin sodium  porcine 100 UNT/ML Injectable Solution': 'Heparin_100',
    'heparin sodium  porcine 1000 UNT/ML Injectable Solution': 'Heparin_1000',
    '0.4 ML Enoxaparin sodium 100 MG/ML Prefilled Syringe': 'Enoxaparin_100',
    '1 ML Enoxaparin sodium 150 MG/ML Prefilled Syringe': 'Enoxaparin_150',
    '1 ML heparin sodium  porcine 5000 UNT/ML Injection': 'Heparin_5000',
    'enoxaparin sodium 100 MG/ML Injectable Solution': 'Enoxaparin_100',
    'Warfarin Sodium 5 MG Oral Tablet': 'Warfarin_5',
    'warfarin sodium 5 MG Oral Tablet': 'Warfarin_5',
    'nan': 'No_medication'
}





def shorten_variable_names(df: pd.DataFrame, 
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
        df[f'{column}_Short'] = df[column].map(rename_map).fillna(df[column])
    
    mapped_count = df[column].isin(rename_map.keys()).sum()
    total_count = len(df)
    print(f"Shortened {mapped_count}/{total_count} variable names ({mapped_count/total_count*100:.1f}%)")
    
    return df


def shorten_variable_names_med(df: pd.DataFrame, 
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

    df[column] = df[column].map(med_map)
    mapped_count = df[column].isin(med_map.keys()).sum()
    total_count = len(df)
    print(f"Shortened {mapped_count}/{total_count} variable names ({mapped_count/total_count*100:.1f}%)")
    
    return df



def shorten_column_names(df: pd.DataFrame, 
                         custom_map: Dict[str, str] = None,
                         show_unmapped: bool = False) -> pd.DataFrame:
    """
    Rename DataFrame columns from long medical names to short descriptive names.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with long column names
    custom_map : Dict[str, str]
        Additional custom mappings to merge with default mappings
    show_unmapped : bool
        If True, print columns that weren't mapped
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with renamed columns
    """
    df = df.copy()
    
    # Merge custom mappings if provided
    rename_map = variable_rename_map.copy()
    if custom_map:
        rename_map.update(custom_map)
    
    # Only rename columns that exist in the mapping
    columns_to_rename = {col: rename_map[col] for col in df.columns if col in rename_map}
    df = df.rename(columns=columns_to_rename)
    
    mapped_count = len(columns_to_rename)
    total_count = len(df.columns)
    print(f"Renamed {mapped_count}/{total_count} columns ({mapped_count/total_count*100:.1f}%)")
    
    if show_unmapped:
        unmapped = [col for col in df.columns if col not in rename_map.values()]
        if unmapped:
            print(f"\nUnmapped columns ({len(unmapped)}):")
            for col in unmapped[:10]:
                print(f"  - {col}")
            if len(unmapped) > 10:
                print(f"  ... and {len(unmapped) - 10} more")
    
    return df



def get_original_name(short_name: str) -> Union[str, None]:
    """Get the original long name from a short name."""
    reverse_map = {v: k for k, v in variable_rename_map.items()}
    return reverse_map.get(short_name)


def get_short_name(long_name: str) -> Union[str, None]:
    """Get the short name from an original long name."""
    return variable_rename_map.get(long_name)


def show_mapping_examples(n: int = 20):
    """Display example mappings for reference."""
    print("Example Variable Name Mappings:")
    print("=" * 80)
    items = list(variable_rename_map.items())[:n]
    for orig, short in items:
        print(f"{orig[:60]:<60} → {short}")
    if len(variable_rename_map) > n:
        print(f"\n... and {len(variable_rename_map) - n} more mappings")


# Example usage:
"""
# For row-based data (DESCRIPTION column)
df = shorten_variable_names(df, column='DESCRIPTION', inplace=False)

# For column-based data (variable names as columns)
df = shorten_column_names(df, show_unmapped=True)

# With custom mappings
custom = {'My Custom Variable': 'Custom_Var'}
df = shorten_column_names(df, custom_map=custom)

# Look up mappings
original = get_original_name('Hemoglobin')  # Returns full name
short = get_short_name('Hemoglobin [Mass/volume] in Blood')  # Returns 'Hemoglobin'

# See examples
show_mapping_examples(30)
"""