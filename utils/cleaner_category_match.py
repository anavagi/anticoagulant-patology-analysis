# Detailed variable categorization (minimal style)
# Generated for use in a Jupyter notebook. Paste into a code cell.
import pandas as pd
from typing import List, Dict
import re

# -------------------------
# Category arrays
# -------------------------

vitals = [
    'Body Height', 'Body Weight', 'Body temperature', 'Body Temperature',
    'Body mass index (BMI) [Ratio]', 'Body mass index (BMI) [Percentile] Per age and sex',
    'Heart rate', 'Respiratory rate', 'Systolic Blood Pressure', 'Diastolic Blood Pressure',
    'Mean blood pressure', 'Oxygen saturation in Arterial blood', 
    'Carbon dioxide [Partial pressure] in Arterial blood',
    'Oxygen [Partial pressure] in Venous blood', 'Carbon dioxide [Partial pressure] in Venous blood',
    'pH of Arterial blood', 'pH of Venous blood', 'Bicarbonate [Moles/volume] in Arterial blood', 
    'Bicarbonate [Moles/volume] in Venous blood','Capillary refill [Time] of Nail bed'
]

hematology = [
    'Leukocytes [#/volume] in Blood by Automated count', 'Erythrocytes [#/volume] in Blood by Automated count',
    'Hemoglobin [Mass/volume] in Blood', 'Hematocrit [Volume Fraction] of Blood by Automated count',
    'Platelets [#/volume] in Blood by Automated count', 'MCV [Entitic volume] by Automated count',
    'MCH [Entitic mass] by Automated count', 'MCHC [Mass/volume] by Automated count',
    'Erythrocyte distribution width [Entitic volume] by Automated count', 'RBC Distribution Width',
    'Platelet distribution width [Entitic volume] in Blood by Automated count',
    'Platelet mean volume [Entitic volume] in Blood by Automated count',
    'Neutrophils [#/volume] in Blood by Automated count', 'Lymphocytes [#/volume] in Blood by Automated count',
    'Monocytes [#/volume] in Blood by Automated count', 'Eosinophils [#/volume] in Blood by Automated count',
    'Basophils [#/volume] in Blood by Automated count',
    'Neutrophils/100 leukocytes in Blood by Automated count', 'Lymphocytes/100 leukocytes in Blood by Automated count',
    'Monocytes/100 leukocytes in Blood by Automated count', 'Eosinophils/100 leukocytes in Blood by Automated count',
    'Basophils/100 leukocytes in Blood by Automated count', 'Hemoglobin', 'Hematocrit', 'MCV', 'Platelet Count'
]

chemistry = [
    'Glucose [Mass/volume] in Blood', 'Glucose [Mass/volume] in Serum or Plasma', 'Glucose [Mass/volume] in Urine by Test strip',
    'Urea nitrogen [Mass/volume] in Blood', 'Urea nitrogen [Mass/volume] in Serum or Plasma',
    'Creatinine [Mass/volume] in Blood', 'Creatinine [Mass/volume] in Serum or Plasma',
    'Calcium [Mass/volume] in Blood', 'Calcium [Mass/volume] in Serum or Plasma',
    'Sodium [Moles/volume] in Blood', 'Sodium [Moles/volume] in Serum or Plasma',
    'Potassium [Moles/volume] in Blood', 'Potassium [Moles/volume] in Serum or Plasma',
    'Chloride [Moles/volume] in Blood', 'Chloride [Moles/volume] in Serum or Plasma',
    'Carbon dioxide  total [Moles/volume] in Blood', 'Carbon dioxide  total [Moles/volume] in Serum or Plasma',
    'Protein [Mass/volume] in Serum or Plasma', 'Albumin [Mass/volume] in Serum or Plasma',
    'Globulin [Mass/volume] in Serum by calculation', 'Bilirubin.total [Mass/volume] in Serum or Plasma',
    'Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma',
    'Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma',
    'Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma',
    'Total Bilirubin (Elevated)', 'ALT (Elevated)', 'AST (Elevated)', 'Anion Gap', 'Magnesium [Mass/volume] in Serum or Plasma',
    'Phosphate [Mass/volume] in Serum or Plasma', 'Iron [Mass/volume] in Serum or Plasma',
    'Iron binding capacity [Mass/volume] in Serum or Plasma', 'Iron saturation [Mass Fraction] in Serum or Plasma',
    'Ferritin [Mass/volume] in Serum or Plasma', 'Lactate dehydrogenase [Enzymatic activity/volume] in Serum or Plasma by Lactate to pyruvate reaction',
    'Creatine kinase [Enzymatic activity/volume] in Serum or Plasma', 'C reactive protein [Mass/volume] in Serum or Plasma',
    'Procalcitonin [Mass/volume] in Serum or Plasma', 'Troponin I.cardiac [Mass/volume] in Serum or Plasma by High sensitivity method',
    'NT-proBNP', 'Magnesium [Mass/volume] in Blood'
]

coagulation = [
    'Prothrombin time (PT)', 'INR in Platelet poor plasma by Coagulation assay', 'aPTT in Blood by Coagulation assay',
    'Activated clotting time (ACT) of Blood by Coagulation assay', 'Fibrin D-dimer FEU [Mass/volume] in Platelet poor plasma'
]

urinalysis = [
    'Appearance of Urine', 'Odor of Urine', 'Clarity of Urine', 'Color of Urine',
    'Glucose [Presence] in Urine by Test strip', 
    'Glucose [Mass/volume] in Urine by Test strip',
    'Ketones [Presence] in Urine by Test strip', 
    'Ketones [Mass/volume] in Urine by Test strip',
    'Specific gravity of Urine by Test strip', 
    'pH of Urine by Test strip',
    'Protein [Presence] in Urine by Test strip', 
    'Protein [Mass/volume] in Urine by Test strip',
    'Nitrite [Presence] in Urine by Test strip', 
    'Hemoglobin [Presence] in Urine by Test strip',
    'Leukocyte esterase [Presence] in Urine by Test strip', 
    'Hemoglobin.gastrointestinal.lower [Presence] in Stool by Immunoassay --1st specimen',
    'Microalbumin/Creatinine [Mass Ratio] in Urine', 
    'Bilirubin.total [Mass/volume] in Urine by Test strip',
    'Bilirubin.total [Presence] in Urine by Test strip', 'WBCs', 'RBCs', 'Epithelial Cells', 'Casts', 'Mucus Threads', 'Bacteria',
    'Bacteria identified in Urine by Culture',
    'Choriogonadotropin (pregnancy test) [Presence] in Urine'
    'Drugs of abuse 5 panel - Urine by Screen method',
    'Choriogonadotropin (pregnancy test) [Presence] in Urine'
]

microbiology = [
    'Influenza virus A Ag [Presence] in Upper respiratory specimen by Rapid immunoassay',
    'Influenza virus B Ag [Presence] in Upper respiratory specimen by Rapid immunoassay',
    'Influenza virus A RNA [Presence] in Respiratory specimen by NAA with probe detection',
    'Influenza virus B RNA [Presence] in Respiratory specimen by NAA with probe detection',
    'SARS-CoV-2 RNA Pnl Resp NAA+probe', 'Respiratory syncytial virus RNA [Presence] in Respiratory specimen by NAA with probe detection',
    'Parainfluenza virus 1 RNA [Presence] in Respiratory specimen by NAA with probe detection',
    'Parainfluenza virus 2 RNA [Presence] in Respiratory specimen by NAA with probe detection',
    'Parainfluenza virus 3 RNA [Presence] in Respiratory specimen by NAA with probe detection',
    'Rhinovirus RNA [Presence] in Respiratory specimen by NAA with probe detection',
    'Human metapneumovirus RNA [Presence] in Respiratory specimen by NAA with probe detection',
    'Adenovirus A+B+C+D+E DNA [Presence] in Respiratory specimen by NAA with probe detection',
    'Gram positive blood culture panel by Probe in Positive blood culture', 'Bacteria identified in Urine by Culture'
]

infectious = [
    'HIV 1 RNA [#/volume] (viral load) in Serum or Plasma by NAA with probe detection', 'HIV 1 Ab [Presence] in Serum',
    'Choriogonadotropin (pregnancy test) [Presence] in Urine',
    'HIV status'
]

immunology_allergy = [
    'Peanut IgE Ab [Units/volume] in Serum', 'Walnut IgE Ab [Units/volume] in Serum',
    'Codfish IgE Ab [Units/volume] in Serum', 'Shrimp IgE Ab [Units/volume] in Serum',
    'Wheat IgE Ab [Units/volume] in Serum', 'Egg white IgE Ab [Units/volume] in Serum',
    'Soybean IgE Ab [Units/volume] in Serum', 'Cow milk IgE Ab [Units/volume] in Serum',
    'White oak IgE Ab [Units/volume] in Serum', 'Common Ragweed IgE Ab [Units/volume] in Serum',
    'Cat dander IgE Ab [Units/volume] in Serum', 'American house dust mite IgE Ab [Units/volume] in Serum',
    'Cladosporium herbarum IgE Ab [Units/volume] in Serum', 'Honey bee IgE Ab [Units/volume] in Serum',
    'Latex IgE Ab [Units/volume] in Serum', 'Toxoplasma gondii Ab [Presence] in Serum'
]

endocrine = [
    'Hemoglobin A1c/Hemoglobin.total in Blood', 'Thyroxine (T4) free [Mass/volume] in Serum or Plasma'
]

cardiology = [
    'Left ventricular Ejection fraction', 'Functional capacity NYHA', 'Objective assessment of cardiovascular disease NYHA',
    'FEV1/FVC', 'Exercise stress test study', 'Oxygen/Total gas setting [Volume Fraction] Ventilator', 'Oxygen [Partial pressure] in Arterial blood'
]

oncology = [
    'Site of distant metastasis in Breast tumor', 'Distant metastases.clinical [Class] Cancer', 'Size.maximum dimension in Tumor',
    'Primary tumor.clinical [Class] Cancer', 'Lymph nodes with macrometastases [#] in Cancer specimen by Light microscopy',
    'Regional lymph nodes.clinical [Class] Cancer', 'HER2 [Presence] in Breast cancer specimen by Immune stain',
    'HER2 [Presence] in Breast cancer specimen by FISH', 'Estrogen receptor Ag [Presence] in Breast cancer specimen by Immune stain',
    'Progesterone receptor Ag [Presence] in Breast cancer specimen by Immune stain',
    'Estrogen+Progesterone receptor Ag [Presence] in Tissue by Immune stain', 'Stage group.clinical Cancer',
    'Tumor marker Cancer', 'Response to cancer treatment', 'Treatment status Cancer',
    'Lymph nodes with micrometastases [#] in Cancer specimen by Light microscopy',
    'Lymph nodes with isolated tumor cells [#] in Cancer specimen by Light microscopy',
    'Weight difference [Mass difference] --pre dialysis - post dialysis','Polyp size greatest dimension'
]

ophthalmology_imaging = [
    'LogMAR visual acuity left eye (observable entity)', 'LogMAR visual acuity right eye (observable entity)',
    'Left eye Diabetic retinopathy severity level by Ophthalmoscopy', 'Right eye Diabetic retinopathy severity level by Ophthalmoscopy',
    'Study observation Left retina by OCT', 'Study observation Right retina by OCT', 'DXA Radius and Ulna [T-score] Bone density'
]

mental_health = [
    'Patient Health Questionnaire-9: Modified for Teens total score [Reported.PHQ.Teen]',
    'Patient Health Questionnaire 9 item (PHQ-9) total score [Reported]', 'Patient Health Questionnaire 2 item (PHQ-2) total score [Reported]',
    'Generalized anxiety disorder 7 item (GAD-7) total score [Reported.PHQ]', #'Total score [DAST-10]', 'Total score [AUDIT-C]',
    'Total score [HARK]',#'PROMIS-10 Global Mental Health (GMH) score',
    #'PROMIS-10 Global Physical Health (GPH) score', 
    'QALY', 'DALY', 'QOLS', 'Overall summary score [KCCQ-12]',
    'Quality of life score [KOOS]', 'Sport-recreation score [KOOS]'
]

social_determinants = [
    #'Tobacco smoking status',
    'Have you been discharged from the armed forces of the United States?',
    'At any point in the past 2 years  has season or migrant farm work been your or your family\'s main source of income?',
    'Are you a refugee?', 'Employment status - current', 'Primary insurance', 'Highest level of education',
    'Address', 'How many people are living or staying at this address?', 'What was your best estimate of the total income of all family members from all sources  before taxes  in last year?',
    'Are you worried about losing your housing?', 'Housing status', 'Has lack of transportation kept you from medical appointments  meetings  work  or from getting things needed for daily living',
    'How often do you see or talk to people that you care about and feel close to (For example: talking to friends on the phone  visiting friends or family  going to church or club meetings)?',
    'In the past year  have you spent more than 2 nights in a row in a jail  prison  detention center  or juvenile correctional facility?',
    'In the past year  have you or any family members you live with been unable to get any of the following when it was really needed?',
    'Do you feel physically and emotionally safe where you currently live?', 'What number best describes how pain has interfered with your general activity during the past week',
    'What number best describes how pain has interfered with your enjoyment of life during the past week',
    'Preferred language', 'How many people are living or staying at this address?',
    'Within the last year  have you been afraid of your partner or ex-partner?',
    'Abuse Status [OMAHA]',
    'Are you covered by health insurance or some other kind of health care plan [PhenX]',
    'Activities of daily living score [KOOS]', 'Pain score [KOOS]'
]

demographics = [
    'Race', 'Do you consider yourself Hispanic/Latino?', 'Sexual orientation', 'Preferred language', 'Age'
]

substance_use = [
    'Drugs of abuse 5 panel - Urine by Screen method', 'Total score [DAST-10]',
    'Withdrawal * as manifested by either of the following: a) Characteristic opioid withdrawal syndrome b) Same (or a closely related) substance is taken to relieve or avoid withdrawal symptoms',
    'Tolerance as defined by either of the following: a) Need for markedly increased amounts of opioids to achieve intoxication or desired effect b) Markedly diminished effect with continued use of the same amount of opioid',
    'Continued use despite knowledge of having a persistent or recurrent physical or psychological problem that is likely to have been caused or exacerbated by opioids.',
    'Recurrent opioid use in situations in which it is physically hazardous', 'Important social  occupational  or recreational activities are given up or reduced because of opioid use',
    'Continued opioid use despite having persistent or recurrent social or interpersonal problems caused or exacerbated by the effects of opioids',
    'Recurrent opioid use resulting in a failure to fulfill major role obligations at work  school  or home', 'Craving or a strong desire to use opioids',
    'A great deal of time is spent in activities necessary to obtain the opioid  use the opioid  or recover from its effects',
    'There is a persistent desire or unsuccessful efforts to cut down or control opioid use',
    'Opioids are often taken in larger amounts or over a longer period than was intended'
]

administrative = [
    'Primary insurance', 'Address', 'Priority Level', 'Operative Status Value', 'Procedure Narrative',
    'History of Hospitalizations+Outpatient visits Narrative', 'Medication management note', 'Mental health Outpatient Note', 
    'Emergency severity index','Mental health Telehealth Note','Priority Level','Symptom', 
]

other = [
    'Left eye Intraocular pressure', 'Right eye Intraocular pressure', 'Study observation Left retina by OCT', 'Study observation Right retina by OCT'
    ,'Pain severity - 0-10 verbal numeric rating [Score] - Reported',
    'Head Occipital-frontal circumference Percentile',
    'Pain severity - Reported',
    'Head Occipital-frontal circumference',
    'Pain severity in the past week - 0-10 numeric rating [Reported]',
    'Fall risk total [Morse Fall Scale]',
    'Fall risk level [Morse Fall Scale]',
    'Cause of Death [US Standard Certificate of Death]',
    'Physical findings of Prostate',
    'Prostate specific Ag [Mass/volume] in Serum or Plasma',
    'US Guidance for biopsy of Prostate',
    'Physical findings of Abdomen by Palpation'
    'VR-36 Bodily pain (BP) score - oblique method',
    'VR-36 General health (GH) score - oblique method'
    'VR-36 Mental health (MH) score - oblique method',
    'VR-36 Physical functioning (PF) score - oblique method',
    'VR-36 Role emotion (RE) score - oblique method',
    'VR-36 Role physical (RP) score - oblique method',
    'VR-36 Social functioning (SF) score - oblique method',
    'VR-36 Vitality (VT) score - oblique method',
    'VR-12 Physical functioning (PF) score - oblique method',
    'VR-12 Role physical (RP) score - oblique method',
    'VR-12 Bodily pain (BP) score - oblique method',
    'VR-12 General health (GH) score - oblique method',
    'VR-12 Vitality (VT) score - oblique method',
    'VR-12 Social functioning (SF) score - oblique method',
    'VR-12 Role emotion (RE) score - oblique method',
    'VR-12 Mental health (MH) score - oblique method',
]

# Medication category keywords
med_category_dict = {
    'antibiotic': ['amoxicillin', 'penicillin', 'cef', 'ciprofloxacin', 'vancomycin', 'azithromycin', 'doxycycline', 'piperacillin', 'clindamycin', 'cephalexin', 'cefuroxime', 'ceftriaxone', 'cefpodoxime', 'fosfomycin', 'aztreonam', 'ampicillin'],
    'analgesic': ['acetaminophen', 'ibuprofen', 'naproxen', 'oxycodone', 'hydrocodone', 'fentanyl', 'tramadol', 'meperidine', 'morphine', 'sufentanil', 'alfentanil'],
    'antihypertensive': ['lisinopril', 'losartan', 'hydrochlorothiazide', 'metoprolol', 'propranolol', 'amlodipine', 'carvedilol', 'nebivolol', 'verapamil', 'atenolol', 'ramipril', 'valsartan', 'bisoprolol', 'pitavastatin'],
    'antidiabetic': ['metformin', 'insulin', 'liraglutide', 'canagliflozin'],
    'hormone': ['ethinyl estradiol', 'levonorgestrel', 'medroxyprogesterone', 'tamoxifen', 'estradiol', 'etonogestrel', 'norethindrone'],
    'statin': ['atorvastatin', 'simvastatin', 'pravastatin', 'rosuvastatin', 'lovastatin', 'pitavastatin'],
    'anticoagulant': ['warfarin', 'heparin', 'enoxaparin', 'dabigatran', 'apixaban', 'rivaroxaban'],
    'inhaler': ['albuterol', 'fluticasone', 'budesonide', 'salmeterol', 'mometasone', 'tiotropium'],
    'immunotherapy': ['rituximab', 'bevacizumab', 'denosumab', 'dornase alfa', 'dysport', 'lenzilumab', 'trastuzumab', 'epirubicin', 'paclitaxel', 'docetaxel', 'cisplatin'],
    'other': []  # default fallback
}

# Flatten list helper
def _flatten_vars(categories: List[str], cat_dict: Dict[str, List[str]]) -> List[str]:
    out = []
    for c in categories:
        out.extend(cat_dict.get(c, []))
    # preserve order, unique
    seen = set(); uniq = []
    for x in out:
        if x not in seen:
            seen.add(x); uniq.append(x)
    return uniq

# Category dictionary
category_dict: Dict[str, List[str]] = {
    'vitals': vitals,
    'hematology': hematology,
    'chemistry': chemistry,
    'coagulation': coagulation,
    'urinalysis': urinalysis,
    'microbiology': microbiology,
    'infectious': infectious,
    'immunology_allergy': immunology_allergy,
    'endocrine': endocrine,
    'cardiology': cardiology,
    'oncology': oncology,
    'ophthalmology_imaging': ophthalmology_imaging,
    'mental_health': mental_health,
    'social_determinants': social_determinants,
    'demographics': demographics,
    'substance_use': substance_use,
    'administrative': administrative,
    'other': other
}

# -------------------------
# Functions to check/add/drop
# -------------------------

def check_categories(df: pd.DataFrame, categories: List[str]) -> Dict[str, Dict[str, List[str]]]:
    result = {}
    for cat in categories:
        vars_in_cat = category_dict.get(cat, [])
        present = [v for v in vars_in_cat if v in df.columns]
        missing = [v for v in vars_in_cat if v not in df.columns]
        result[cat] = {'present': present, 'missing': missing}
    return result


def drop_categories(df: pd.DataFrame, categories: List[str], column: str = 'DESCRIPTION', fuzzy: bool = True) -> pd.DataFrame:
    """Drop rows whose DESCRIPTION matches any variable in the given categories."""
    cols = _flatten_vars(categories, category_dict)
    
    if fuzzy:
        # Build a regex pattern for partial, case-insensitive matches
        escaped = [re.escape(c) for c in cols]
        pattern = '|'.join(escaped)
        mask = df[column].str.contains(pattern, case=False, regex=True, na=False)
    else:
        mask = df[column].isin(cols)
    
    dropped = mask.sum()
    print(f"Dropping {dropped} rows from categories: {categories}")
    if dropped > 0:
        print(f"Sample of dropped values: {list(df[mask][column].unique()[:5])}")
    
    return df[~mask].reset_index(drop=True)


def drop_category_columns(df: pd.DataFrame, categories: List[str]) -> pd.DataFrame:
    """Drop COLUMNS (not rows) that match any variable in the given categories."""
    cols_to_drop = _flatten_vars(categories, category_dict)
    
    # Find which columns actually exist in the dataframe
    existing_cols = [c for c in cols_to_drop if c in df.columns]
    
    print(f"Dropping {len(existing_cols)} columns from categories: {categories}")
    if existing_cols:
        print(f"Sample columns being dropped: {existing_cols[:5]}")
    
    return df.drop(columns=existing_cols)


def diagnose_category_match(df: pd.DataFrame, category: str, column: str = 'DESCRIPTION'):
    """Diagnose why categories might not be matching."""
    cat_vars = category_dict.get(category, [])
    
    print(f"\n=== Diagnosis for category: {category} ===")
    print(f"Variables in category: {len(cat_vars)}")
    print(f"Unique values in df['{column}']: {df[column].nunique()}")
    
    # Check for exact matches
    exact_matches = set(df[column].unique()).intersection(set(cat_vars))
    print(f"\nExact matches found: {len(exact_matches)}")
    if exact_matches:
        print(f"Examples: {list(exact_matches)[:3]}")
    
    # Check for partial matches (case-insensitive)
    partial_matches = []
    for val in df[column].unique():
        for cat_var in cat_vars:
            if cat_var.lower() in str(val).lower() or str(val).lower() in cat_var.lower():
                partial_matches.append(val)
                break
    
    print(f"\nPartial matches found: {len(set(partial_matches))}")
    if partial_matches:
        print(f"Examples: {list(set(partial_matches))[:3]}")
    
    if not exact_matches and not partial_matches:
        print("\n⚠️ NO MATCHES FOUND!")
        print(f"Sample category variables: {cat_vars[:3]}")
        print(f"Sample df values: {list(df[column].unique()[:3])}")


def add_categories(df: pd.DataFrame, categories: List[str], fill_value=pd.NA) -> pd.DataFrame:
    cols = _flatten_vars(categories, category_dict)
    for c in cols:
        if c not in df.columns:
            df[c] = fill_value
    return df


def categorize_meds(df: pd.DataFrame, column: str = 'DESCRIPTION') -> pd.DataFrame:
    """
    Adds a 'MED_CATEGORY' column based on keywords in the medication description.
    """
    def find_category(desc):
        desc_lower = str(desc).lower()
        for cat, keywords in med_category_dict.items():
            if any(k.lower() in desc_lower for k in keywords):
                return cat
        return 'other'
    
    df['MED_CATEGORY'] = df[column].apply(find_category)
    return df

def drop_meds_by_category(df: pd.DataFrame, categories: List[str]) -> pd.DataFrame:
    mask = df['MED_CATEGORY'].isin(categories)
    print(f"Dropping {mask.sum()} medications from categories: {categories}")
    if mask.sum() > 0:
        print(f"Sample dropped: {list(df[mask]['DESCRIPTION'].unique()[:5])}")
    return df[~mask].reset_index(drop=True)