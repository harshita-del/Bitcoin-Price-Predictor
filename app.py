import streamlit as st
import joblib
import pandas as pd

model = joblib.load("bitcoin_model.pkl")

st.title("Bitcoin Price Predictor")

price = st.number_input("Enter today's Bitcoin closing price")

if st.button("Predict"):
    data = pd.DataFrame({"Close": [price]})
    prediction = model.predict(data)
    st.success(f"Predicted next day price: ${prediction[0]:,.2f}")
