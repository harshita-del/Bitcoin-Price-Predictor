import streamlit as st
import joblib
import pandas as pd

model = joblib.load("bitcoin_model.pkl")

st.title("Bitcoin Price Predictor")

st.write(
    "Predict the next day's Bitcoin closing price using a Linear Regression model trained on historical Bitcoin data."
)

st.info("Model R² Score: 0.9894")

price = st.number_input(
    "Enter today's Bitcoin closing price",
    min_value=0.0,
    value=40000.0
)

if st.button("Predict"):

    data = pd.DataFrame({"Close": [price]})

    prediction = model.predict(data)

    st.success(
        f"Predicted next day Bitcoin price: ${prediction[0]:,.2f}"
    )
