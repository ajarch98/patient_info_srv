import streamlit as st
from entities.hospital import Hospital
from entities.patient import Patient


st.title("Data Collection Form")

# Patient details
st.header("Patient details")

patient_name = st.text_input("Patient Name")
patient_age = st.text_input("Patient age")

# Hospital details
st.header("Hospital details")

hospital_name = st.text_input("Hospital Name")
hospital_location = st.text_input("Hospital location")

