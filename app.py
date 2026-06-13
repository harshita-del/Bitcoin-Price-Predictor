import streamlit as st
import joblib
import pandas as pd

model = joblib.load("bitcoin_model.pkl")

st.title("Bitcoin Price Predictor")

open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")
low_price = st.number_input("Low Price")
close_price = st.number_input("Close Price")
volume = st.number_input("Volume")

if st.button("Predict"):

    data = pd.DataFrame({
        "Open": [open_price],
        "High": [high_price],
        "Low": [low_price],
        "Close": [close_price],
        "Volume": [volume]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Next Day Price: ${prediction[0]:,.2f}")
