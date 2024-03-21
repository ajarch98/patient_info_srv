from entities.patient import Patient

# Create a patient instance to test

patient1 = Patient(id="1001", name="John Doe", age=35, gender="Male", address="123 Main St",
                   phone="555-1234", email="john@example.com", date_of_birth="1986-01-01",
                   nationality="American", marital_status="Single", occupation="Engineer",
                   medical_history="", allergies="swag", medications="pussy", blood_type="O+",
                   insurance_info="ABC Health", primary_care_physician="Dr. Smith",
                   emergency_contact="Jane Doe (555-5678)")


def print_record(patient):
    """Prints the record of a patient instance"""
    record = f"id: {patient.id}\n"
    record = f"Name: {patient.name}\n"
    record += f"Age: {patient.age}\n"
    record += f"Gender: {patient.gender}\n"
    record += f"Address: {patient.address}\n"
    record += f"Phone: {patient.phone}\n"
    record += f"Email: {patient.email}\n"
    record += f"Date of Birth: {patient.date_of_birth}\n"
    record += f"Nationality: {patient.nationality}\n"
    record += f"Marital Status: {patient.marital_status}\n"
    record += f"Occupation: {patient.occupation}\n"
    record += f"Medical History: {patient.medical_history}\n"
    record += f"Allergies: {patient.allergies}\n"
    record += f"Medications: {patient.medications}\n"
    record += f"Blood Type: {patient.blood_type}\n"
    record += f"Insurance Info: {patient.insurance_info}\n"
    record += f"Primary Care Physician: {patient.primary_care_physician}\n"
    record += f"Emergency Contact: {patient.emergency_contact}\n"
    return record

def print_records(patients):
    """Prints records for all patients in a list"""
    if not patients:
        print("Patient records are empty")
    else:
        for idx, patient in enumerate(patients, start=1):
            print(f"Patient {idx} Record:")
            print(print_record(patient))
            print()

print_records(patients=[patient1])