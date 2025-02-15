#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("xgboost_obesity_model.pkl")

# Streamlit UI
st.title("Obesity Prediction App")

# User input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=100, value=25)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=70)
family_history = st.selectbox("Family History of Obesity", ["Yes", "No"])
FAVC = st.selectbox("Frequent Consumption of High-Calorie Foods", ["Yes", "No"])
FCVC = st.slider("Vegetable Consumption Frequency (1-3)", 1, 3, 2)
NCP = st.slider("Number of Main Meals Per Day", 1, 4, 3)
CAEC = st.selectbox("Consumption of Food Between Meals", ["No", "Sometimes", "Frequently", "Always"])
SMOKE = st.selectbox("Do you smoke?", ["Yes", "No"])
CH2O = st.slider("Daily Water Intake (Liters)", 1, 3, 2)
SCC = st.selectbox("Calories Consumption Monitoring", ["Yes", "No"])
FAF = st.slider("Physical Activity Frequency (0-3)", 0, 3, 1)
TUE = st.slider("Time Using Technology Devices (0-2)", 0, 2, 1)
CALC = st.selectbox("Alcohol Consumption", ["No", "Sometimes", "Frequently", "Always"])
MTRANS = st.selectbox("Main Transportation Mode", ["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"])

# Convert categorical inputs to numerical values
mapping = {"Yes": 1, "No": 0, "Male": 1, "Female": 0,
           "No": 0, "Sometimes": 1, "Frequently": 2, "Always": 3,
           "Automobile": 0, "Bike": 1, "Motorbike": 2, "Public_Transportation": 3, "Walking": 4}

def encode(value):
    return mapping.get(value, value)

input_data = np.array([
    encode(gender), age, height, weight, encode(family_history), encode(FAVC),
    FCVC, NCP, encode(CAEC), encode(SMOKE), CH2O, encode(SCC), FAF, TUE,
    encode(CALC), encode(MTRANS)
]).reshape(1, -1)

if st.button("Predict Obesity Level"):
    prediction = model.predict(input_data)[0]
    st.write(f"Predicted Obesity Level: {prediction}")


# In[ ]:




