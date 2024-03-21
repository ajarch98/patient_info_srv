class Patient:
    def __init__(self, name: str, age: int, gender: str, address: str, phone: str, email: str,
                 date_of_birth: str, nationality: str, marital_status: str, occupation: str,
                 medical_history: str, allergies: str, medications: str, blood_type: str,
                 insurance_info: str, primary_care_physician: str, emergency_contact: str, id: int):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone
        self.email = email
        self.date_of_birth = date_of_birth
        self.nationality = nationality
        self.marital_status = marital_status
        self.occupation = occupation
        self.medical_history = medical_history
        self.allergies = allergies
        self.medications = medications
        self.blood_type = blood_type
        self.insurance_info = insurance_info
        self.primary_care_physician = primary_care_physician
        self.emergency_contact = emergency_contact
