import pandas as pd
import numpy as np
from typing import Dict

def get_first_non_null(series: pd.Series) -> any:
  
    non_null_values = series.dropna()
    if not non_null_values.empty:
        return non_null_values.iloc[0]
    return np.nan

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:

    name_map = [
        # Variables Clau
        ("CODI_PACIENT", "CODI_PACIENT"),
        ("INR", "INR"),

        # Funció Hepàtica
        ("ALANINA AMINOTRANSFERASA", "ALT_GPT"),
        ("ALT (GPT)", "ALT_GPT"),
        ("Alanina aminotransferasa", "ALT_GPT"),
        ("Alanina aminotranferasa (ALAT), suero", "ALT_GPT"),
        ("Srm-ALANINA AMINOTRANSFERASA", "ALT_GPT"),
        ("Srm-Alanina-aminotransferasa", "ALT_GPT"), 
        ("Srm-Alanina-aminotransferasa; b", "ALT_GPT"), 
        ("SrmAlanina-aminotransferasa; c.cat.", "ALT_GPT"), 
        ("Srm_Alanina-aminotransferasa; c. cat. (IFCC)", "ALT_GPT"), 
        ("Srm_Alanina-aminotransferasa; c. cat.#(IFCC)", "ALT_GPT"), 
        ("ASPARTAT AMINOTRANSFERASA", "AST_GOT"),
        ("ASPARTATO AMINOTRANSFERASA (AST) (GOT)", "AST_GOT"), 
        ("ASPARTATO AMINOTRANSFERASA (GOT/AST), SUERO", "AST_GOT"), 
        ("AST (GOT)", "AST_GOT"),
        ("Aspartat aminotransferasa", "AST_GOT"),
        ("Srm-Aspartat", "AST_GOT"),
        ("Aspartat aminotranferasa (AST) sèrum", "AST_GOT"), 
        ("Aspartat aminotranferasa (AST) sèrum (1920-8)", "AST_GOT"), 
        ("GOT (AST) SERUM", "AST_GOT"), 
        ("SrmAspartat-aminotransferasa; c.cat.", "AST_GOT"), 
        ("BILIRUBINA TOTAL, SUERO", "BILIRUBINA_TOTAL"), 
        ("Bilirrubina total, suero", "BILIRUBINA_TOTAL"), 
        ("BILIRUBINA", "BILIRUBINA_TOTAL"),
        
        # Funció Renal i Electròlits
        ("CREATININ", "CREATININA"),
        ("CREATININA", "CREATININA"),
        ("Srm-CREATININI", "CREATININA"),
        ("UREA", "UREA"),
        ("POTASSI", "POTASSI"),
        ("POTASIO", "POTASSI"),
        ("Srm-Ió Potassi", "POTASSI"),
        ("Potasi (K) Sèric", "POTASSI"), 
        ("SODI", "SODI"),
        ("SODIO", "SODI"),
        ("Srm-Ió Sodi", "SODI"),
        ("CALCI", "CALCI"),
        ("CALCIO", "CALCI"),
        ("CLORUR", "CLORUR"),
        ("CLOR", "CLORUR"),
        ("CLORURO", "CLORUR"),

        # Marcadors Metabòlics
        ("GLUCOSA", "GLUCOSA"),
        ("GLUCEMIA", "GLUCOSA"),
        ("Srm-GLUCOSA", "GLUCOSA"),
        ("Glicèmia venosa dejú", "GLUCOSA"), 
        ("HEMOGLOBINA GLICOSILADA", "HB_GLICOSILADA_A1C"),
        ("GLICOHEMOGLOBINA", "HB_GLICOSILADA_A1C"),
        ("Hb(San)-Glicohemoglobina", "HB_GLICOSILADA_A1C"),
        ("HB GLICOSILADA (A1c) Sang", "HB_GLICOSILADA_A1C"), 
        ("Colesterol total", "COLESTEROL_TOTAL"), 

        # Altres Biomarcadors
        ("FOSFATASA ALCALINA", "FOSFATASA_ALCALINA"),
        ("FILTRAT GLOMERULAR", "FG_CKD_EPI"),
        ("F. G. ESTIMAT", "FG_CKD_EPI"),
        ("CKD-EPI", "FG_CKD_EPI"),
        ("Filtrado glomerular", "FG_CKD_EPI"), 
        ("FERRITINA", "FERRITINA"),
        ("FERRO", "FERRO"),
        ("HIERRO", "FERRO"),
        ("SIDEREMIA", "FERRO"),
        ("CREATINA CINASA", "CREATINA_KINASA_CK"),
        ("CREATINA KINASA", "CREATINA_KINASA_CK"),
        ("CREATINA-CINASA (CK), SUERO", "CREATINA_KINASA_CK"), 
        ("Srm-Creatina-cinasa", "CREATINA_KINASA_CK"), 
        ("LDH", "LDH"),
        ("Srm-Lactat-deshidrogenasa", "LDH"), 
        ("Srm_Lactat-deshidrogenasa; c.cat. #(IFCC)", "LDH"), 
        ("Srml-Lactat-deshidrogenasa; c.cat.", "LDH"), 
        ("MAGNESI", "MAGNESI"),
        ("MAGNESIO", "MAGNESI"),
        ("PROTEINA C REACTIVA", "PCR"),
        ("PROTEÏNA C REACTIVA", "PCR"),
        ("PROTEÍNA C REACTIVA, SUERO", "PCR"), 
        ("PROTEINAS TOTALES", "PROTEINES_TOTALS"),
        ("PROTEÏNES TOTALS", "PROTEINES_TOTALS"),
        ("PROTEINES_TOTALS", "PROTEINES_TOTALS"),
        ("Proteínas, suero", "PROTEINES_TOTALS"), 
        ("Proteïna-Sèrum", "PROTEINES_TOTALS"), 
        ("Srm-Proteïna", "PROTEINES_TOTALS"), 
        ("SrmProteïna; c.massa", "PROTEINES_TOTALS"), 
        ("Srm_Proteïna; c.massa", "PROTEINES_TOTALS"), 
        ("PRECURSOR DEL PÉPTIDO NATRIURÉTICO CEREBRAL", "NT_PROBNP"),
        ("Pro-Pèptid natriurètic cerebral (1-76); c.massa", "NT_PROBNP"), 
        ("Microalbuminuria", "MICROALBUMINURIA"),
        ("Uri-Albúmina", "MICROALBUMINURIA"),
        ("ALBÚMINA (MAU) ORINA", "MICROALBUMINURIA"), 
        ("ALBÚMINA  (MAU) ORINA", "MICROALBUMINURIA"), 
        ("ALBÚMINA Orina esporádica", "MICROALBUMINURIA"), 
        ("O Albúmina; c.massa", "MICROALBUMINURIA"), 
        ("Dímer D de la fibrina; c.massa (immunoquímica)", "DIMER_D"), 
        ("Troponina I alta sensibilitat (VRef <45 ng/L)", "TROPONINA_I_ALTA_SENSIBILITAT"), 
        ("Srm-Troponina I alta sensibilitat", "TROPONINA_I_ALTA_SENSIBILITAT"), 

        # Hemograma - Variables Entèriques
        ("Ample Distribució Eritrocits", "RDW_CV"),
        ("Amplitud distribució eritrocitària", "RDW_CV"),
        ("RDW", "RDW_CV"),
        ("R.D.W.", "RDW_CV"), 
        ("Amplitud de distribució eritrocitària-Sang", "RDW_CV"), 
        ("Ers(San)-A. D. E.", "RDW_CV"), 
        ("Conc.Hb.Corpuscular Media", "CHCM"),
        ("Concentració Hemoglobina corpuscular mitjana", "CHCM"),
        ("CCMH", "CHCM"),
        ("HEMOGLOBINA (CCMH)", "CHCM"),
        ("C H C M", "CHCM"), 
        ("CHCM (786-4)", "CHCM"), 
        ("Concentració HGB Corpuscular mitja", "CHCM"), 
        ("M. C. H. C.", "CHCM"), 
        ("M.C.H.C.", "CHCM"), 
        ("San-CONC.HGB.CORP. MITJA, p", "CHCM"), 
        ("H. C. M.", "HCM"),
        ("Hemoglobina corpuscular mitja", "HCM"),
        ("HEMOGLOBINA (HCM)", "HCM"),
        ("Hb.Corpuscular Media", "HCM"), 
        ("Ers(San)-Hb. corp. mitjana (HCM); m", "HCM"), 
        ("M.C.H.", "HCM"), 
        ("Volum corpuscular mig", "VCM"),
        ("Vol. corp.mitjà (VCM)", "VCM"),
        ("Volum eritrocític", "VCM"),
        ("VCM", "VCM"),
        ("Ers(San)-V. C. M.", "VCM"), 
        ("V C M", "VCM"), 
        ("V. C. M.", "VCM"), 
        ("VCM (787-2)", "VCM"), 
        ("Volum corpuscular mitjà-Sang", "VCM"), 
        ("San-VOLUM CORPUSCULAR MITJÀ, v", "VCM"), 
        ("Volumen corpuscular medio", "VCM"), 
        ("Amplitud de distribució plaquetària", "VPM"), # Assumint que és VPM
        ("Volum plaquetar mig", "VPM"),
        ("VPM", "VPM"),
        ("Plaquetari mitjà", "VPM"),  
        ("Pqs(San)-V. P. M.", "VPM"), 
        ("San-VOLUM PLAQUETARI MITJÀ", "VPM"), 
        ("Volum plaquetari mig", "VPM"),
        ("Volum plaquetari mitjà-Sang", "VPM"), 
        ("V. P. M.", "VPM"),
        ("P. D. W.", "PDW"), 
        ("PDW", "PDW"), 

        # Hemograma - Cèl·lules i Percentatges
        ("LEUCÒCITS", "LEUCOCITS"),
        ("Leucocitos", "LEUCOCITS"),
        ("HEMATIES", "HEMATIES"),
        ("Eritròcits", "HEMATIES"),
        ("Hematíes", "HEMATIES"), 
        ("HEMATÒCRIT", "HEMATOCRIT"),
        ("Hematocrito", "HEMATOCRIT"),
        ("HEMOGLOBINA", "HEMOGLOBINA"),
        ("Plaquetes", "PLAQUETES"),
        ("PLAQUETAS", "PLAQUETES"),
        
        # Hemograma - Diferencial
        ("BASÒFILS", "BASOFILS_PCT"),
        ("Basófilos aut%", "BASOFILS_PCT"),
        ("BASOFILS:(%)", "BASOFILS_PCT"), 
        ("Basófilos %", "BASOFILS_PCT"), 
        ("EOSINÒFILS", "EOSINOFILS_PCT"),
        ("Eosinófilos aut%", "EOSINOFILS_PCT"),
        ("EOSINOFILS:(%)", "EOSINOFILS_PCT"), 
        ("Eosinófilos %", "EOSINOFILS_PCT"), 
        ("LIMFÒCITS", "LIMFOCITS_PCT"),
        ("Linfocitos aut%", "LIMFOCITS_PCT"),
        ("LIMFOCITS:(%)", "LIMFOCITS_PCT"), 
        ("Linfocitos %", "LIMFOCITS_PCT"), 
        ("MONÒCITS", "MONOCITS_PCT"),
        ("Monocitos aut%", "MONOCITS_PCT"),
        ("MONOCITS:(%)", "MONOCITS_PCT"), 
        ("Monocitos %", "MONOCITS_PCT"), 
        ("NEUTRÒFILS", "NEUTROFILS_PCT"),
        ("Neutrófilos", "NEUTROFILS_PCT"),
        ("NEUTROFILS:(%)", "NEUTROFILS_PCT"), 

        # Variables objecte (no es fusionen, però es netegen)
        ("Pressió Arterial Diastòlica", "PAD"),
        ("Pressió Arterial Sistòlica", "PAS"),
        ("Freqüència cardíaca", "FREQ_CARDIACA"),
        ("Ritme cardíac", "FREQ_CARDIACA"),
        ("Pes", "PES"),
        ("IMC", "IMC"),
        ("Cigarretes/dia", "CIGARRETES_DIA"),
        ("Ara fuma?", "FUMADOR_ACTIU"),
        ("Tipus d'intervenció tabac", "INTERVENCIÓ_TABAC"),
        ("Cribratge abús alcohol", "CRIBRATGE_AUDIT_C"),
        ("Etapa canvi. Activitat física", "ESTAT_ACTIVITAT_FISICA"),
        ("Qüestionari CBPAAT d'activitat física", "CBPAAT"),
        ("Temps assegut (h/d)", "TEMPS_SEDESTACIO_H_D"),
        ("Activitat exercici en consulta", "ACTIVITAT_EXERCICI_CONSULTA"),
        ("Consell consum d'alcohol", "CONSELL_CONSUM_ALCOHOL"), 
        ("Cribratge alimentació", "CRIBRATGE_ALIMENTACIÓ"), 
        ("Motivació tabac", "MOTIVACIÓ_TABAC"), 
        ("Paquets/any consumits", "PAQUETS_ANY_CONSUMITS"), 
        ("Sedestació interrompuda", "SEDESTACIÓ_INTERROMPUDA"), 
        ("Test dep. nicotina (Fagerström) breu", "TEST_FAGERSTRÖM_BREU"), 
        ("Tipus d'exposició ambiental de tabac", "EXPOSICIÓ_AMBIENTAL_TABAC"), 
        ("Valoració resultat AUDIT-C", "VALORACIÓ_AUDIT_C"), 
        ("Voldria deixar de fumar?", "VOLDRIA_DEIXAR_FUMAR"), 
        ("DIAGNÒSTIC ASSOCIAT", "DIAGNÒSTIC_ASSOCIAT"), 
    ]
    
    # 1. Crear un diccionari de mapeig de columnes netes
    column_mapping: Dict[str, str] = {}
    
    # 2. Recórrer les columnes del DataFrame per trobar el nom net corresponent
    for original_col in df.columns:
        # Normalitzem el nom per facilitar la cerca (sense accents, minúscules, espais)
        normalized_col = original_col.upper().replace(' ', '_').replace('.', '_').replace('-', '_').replace('(SÈRUM);_C_CAT', '').replace(';', '').replace(',', '').strip()

        found_match = False
        for pattern, clean_name in name_map:
            # Utilitzem 'in' per fer la coincidència parcial
            if pattern.upper() in original_col.upper() or pattern.upper() in normalized_col:
                column_mapping[original_col] = clean_name
                found_match = True
                break
        
        if not found_match:
            # Per a les columnes que no coincideixen, les mantenim (o les netegem bàsicament)
            column_mapping[original_col] = original_col.strip() 

    # 3. Aplicar el reanomenament
    df = df.rename(columns=column_mapping)
    
    # 4. Gestionar les columnes duplicades (diferents noms sorollosos que han mapejat al mateix nom net)
    # Per a les columnes que ara tenen el mateix nom net, hem de fusionar-les:
    
    # Agrupem els noms nets per veure quins es van duplicar
    duplicates = df.columns[df.columns.duplicated(keep=False)].unique()
    
    for clean_name in duplicates:
        # Selecciona totes les columnes que van acabar amb el mateix nom net
        cols_to_merge = df.loc[:, df.columns == clean_name]
        
        # Aplica la lògica de fusió: pren el primer valor no nul de cada fila
        # Axis 1 (fila) perquè estem fusionant columnes en una sola
        df[clean_name] = cols_to_merge.apply(get_first_non_null, axis=1)
        
        # Elimina les columnes originals fusionades (totes menys la nova columna neta)
        df = df.loc[:, (df.columns != clean_name) | (df.columns.duplicated(keep='first'))]


    # Aquest pas final elimina les columnes que no eren úniques i no es van fusionar
    # Correcte si es fa abans del següent pas
    df = df.loc[:, ~df.columns.duplicated()]
    
    return df

def process_lab_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció principal per processar el DataFrame de dades de laboratori:
    1. Estandaritza els noms de les columnes.
    2. Fusiona els registres duplicats per CODI_PACIENT, prioritzant 
       conservar tots els valors no nuls en una sola fila.
    
    :param df: DataFrame de Pandas amb les dades de laboratori i un CODI_PACIENT.
    :return: DataFrame net i fusionat amb un registre únic per pacient.
    """
    print("Iniciant el processament de les dades...")

    # Pas 1: Estandaritzar i fusionar les columnes amb noms sorollosos
    df_cleaned = standardize_column_names(df.copy())
    
    # Comprovem que CODI_PACIENT existeix després de la neteja
    if 'CODI_PACIENT' not in df_cleaned.columns:
        print("Error: La columna 'CODI_PACIENT' no es va trobar després de la neteja de noms.")
        return df_cleaned

    print(f"Columnes estandarditzades. {len(df.columns)} columnes originals -> {len(df_cleaned.columns)} columnes netes.")

    # Pas 2: Fusionar registres duplicats (un registre únic per CODI_PACIENT)
    
    # Identificar les columnes per aplicar la funció d'agregació
    # Excloent el CODI_PACIENT (que és la clau de l'agrupació)
    cols_to_aggregate = [col for col in df_cleaned.columns if col != 'CODI_PACIENT']

    # Crear un diccionari amb la funció d'agregació desitjada per a cada columna
    # Utilitzem 'get_first_non_null' per fusionar dades no nules a la mateixa fila
    agg_funcs = {col: get_first_non_null for col in cols_to_aggregate}
    
    # Realitzar l'agrupació i l'agregació
    df_merged = df_cleaned.groupby('CODI_PACIENT', as_index=False).agg(agg_funcs)

    # Imprimir estadístiques de fusió
    original_rows = len(df)
    merged_rows = len(df_merged)
    print(f"Fusió completada. Files originals: {original_rows}. Registres únics de pacient: {merged_rows}.")
    
    return df_merged

