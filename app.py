import streamlit as st
import numpy as np
from model import train

st.title("Exam Score Predictor App")
st.subheader("Predict your marks based on study hours")

model = train()

st.sidebar.header("Input Features")
study_hours = st.sidebar.slider("Select study hours", 1, 10, 1)

input_array = np.array([[study_hours]])
Prediction = model.predict(input_array)

st.write(f'### Study Hours : {study_hours}')
# Using [0][0] here to prevent the formatting error you faced last time!
st.write(f'### Predicted Score: {Prediction[0]:.2f}')