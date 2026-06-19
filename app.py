
import streamlit as st
import pandas as pd
import pickle

df = pd.read_csv("Salary Data.csv").dropna()

model = pickle.load(open("salary_model.pkl", "rb"))
genders = pickle.load(open("genders.pkl", "rb"))
educations = pickle.load(open("educations.pkl", "rb"))
jobs = pickle.load(open("jobs.pkl", "rb"))
gender_encoder = pickle.load(open("gender_encoder.pkl", "rb"))
education_encoder = pickle.load(open("education_encoder.pkl", "rb"))
job_encoder = pickle.load(open("job_encoder.pkl", "rb"))

st.title("Salary Predictor")

age = st.number_input("Age", 18, 70, 25)
gender = st.selectbox("Gender", genders)
education = st.selectbox("Education Level", educations)
job = st.selectbox("Job Title", jobs)
experience = st.slider("Years of Experience", 0, 40, 2)

if st.button("Predict Salary"):
    gender_encoded = gender_encoder.transform([gender])[0]
    education_encoded = education_encoder.transform([education])[0]
    job_encoded = job_encoder.transform([job])[0]

    employee = pd.DataFrame({
        'Age': [age],
        'Gender': [gender_encoded],
        'Education Level': [education_encoded],
        'Job Title': [job_encoded],
        'Years of Experience': [experience]
    })

    prediction = model.predict(employee)[0]

    st.success(f"Predicted Salary : ₹{prediction:,.2f}")

    percentile = (df['Salary'] < prediction).mean() * 100
    st.write(f"You are in the top {100 - percentile:.2f}% earners")

    salaries = []
    for exp in range(1, 11):
        temp = pd.DataFrame({
            'Age': [age],
            'Gender': [gender_encoded],
            'Education Level': [education_encoded],
            'Job Title': [job_encoded],
            'Years of Experience': [exp]
        })
        sal = model.predict(temp)[0]
        salaries.append(sal)

    growth = pd.DataFrame({
        'Experience': list(range(1, 11)),
        'Salary': salaries
    })

    st.subheader("Salary Growth (1–10 Years)")
    st.line_chart(growth.set_index('Experience'))