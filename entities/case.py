class Case:
    def __init__(self, case_id: int, patient_id: int, hospital_id: int, icd10_code: str, surgery_catalog: str):
        self.case_id = case_id
        self.patient_id = patient_id
        self.hospital_id = hospital_id
        self.icd10_code = icd10_code
        self.surgery_catalog = surgery_catalog

        # Initialize subcategories
        self.icd10 = ICD10(icd10_code)
        self.surgery = SurgeryCatalog(surgery_catalog)

#split up ICD10 AND SurgeryCatolog, hunch that it might be easier later
class ICD10:
    def __init__(self, code: str):
        self.code = code

class SurgeryCatalog:
    def __init__(self, catalog: str):
        self.catalog = catalog
