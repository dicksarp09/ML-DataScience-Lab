#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import joblib


# Load the trained model
model = joblib.load(r"C:\Users\Dickson\Desktop\ML project\4. Support vector Machine\breast_cancer_model.pkl")

# Streamlit App Title
st.title("Breast Cancer Prediction App")

# Input fields for user data
st.write("Enter the following details to predict:")
mean_radius = st.number_input("Mean Radius", min_value=0.0, format="%.2f")
mean_texture = st.number_input("Mean Texture", min_value=0.0, format="%.2f")
mean_perimeter = st.number_input("Mean Perimeter", min_value=0.0, format="%.2f")
mean_area = st.number_input("Mean Area", min_value=0.0, format="%.2f")
mean_smoothness = st.number_input("Mean Smoothness", min_value=0.0, format="%.4f")

# Predict button
if st.button("Predict"):
    # Arrange inputs as a feature vector
    input_features = [[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]]
    
    # Perform prediction
    prediction = model.predict(input_features)
    prediction_label = "Malignant" if prediction[0] == 1 else "Benign"

    # Display prediction result
    st.write(f"Prediction: **{prediction_label}**")


# In[ ]:




