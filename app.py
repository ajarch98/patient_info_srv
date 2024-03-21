import streamlit as st
from entities.hospital import Hospital
from entities.patient import Patient

st.set_page_config(layout="wide")

st.title("Data Collection Form")

# Creating Columns because aesthetics
left_column, right_column = st.columns(2)

with left_column:    
    
    st.header("Patient Details")
    
    # Patient details
    split_columns1,split_columns2 = st.columns(2)
    
    with split_columns1:
        patient_id = st.text_input("Patient ID")
        patient_age = st.text_input("Patient Age")
        patient_phone = st.text_input("Phone")
        patient_email = st.text_input("Email")
        patient_date_of_birth = st.date_input("Date of Birth")
        patient_blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        patient_nationality = st.text_input("Nationality")
        patient_occupation = st.text_input("Occupation")
        patient_address = st.text_area("Address")
        
        patient_emergency_contact = st.text_input("Emergency Contact")
        
    with split_columns2:
        patient_name = st.text_input("Patient Name")
        patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        patient_marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
        patient_primary_care_physician = st.text_input("Primary Care Physician")
        patient_medical_history = st.text_area("Medical History")
        patient_allergies = st.text_area("Allergies")
        patient_medications = st.text_area("Medications")
        patient_insurance_info = st.text_area("Insurance Info")
        
with right_column:
    
    # Hospital details
    
    st.header("Hospital Details")
    hospital_name = st.text_input("Hospital Name")
    hospital_address = st.text_input("Hospital Address")
    hospital_city = st.text_input("Hospital City")
    hospital_state = st.text_input("Hospital State")
    hospital_zipcode = st.text_input("Hospital Zipcode")
    hospital_phone = st.text_input("Hospital Phone")
    hospital_email = st.text_input("Hospital Email")
    hospital_website = st.text_input("Hospital Website")
    submit_button_label = "Submit"
    submit_button = st.button(submit_button_label,)


if submit_button:
    hospital = Hospital(name=hospital_name, address=hospital_address, city="", state="",
                        zipcode="", phone="", email="", website="")
    
    patient = Patient(name=patient_name, age=patient_age, gender=patient_gender, address=patient_address,
                      phone=patient_phone, email=patient_email, date_of_birth=patient_date_of_birth,
                      nationality=patient_nationality, marital_status=patient_marital_status,
                      occupation=patient_occupation, medical_history=patient_medical_history,
                      allergies=patient_allergies, medications=patient_medications,
                      blood_type=patient_blood_type, insurance_info=patient_insurance_info,
                      primary_care_physician=patient_primary_care_physician,
                      emergency_contact=patient_emergency_contact, id=patient_id)
    
    st.success("Data submitted successfully!")
    

    
