
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))

st.title("Student Score Predictor")

hours = st.number_input("Hours Studied")
sleep = st.number_input("Sleep Hours")
att = st.number_input("Attendance")

if st.button("Predict"):
    result = model.predict([[hours,sleep,att]])
    st.write("Predicted Score:", result[0])
