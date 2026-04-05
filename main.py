import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.model import predict_temp

st.set_page_config(page_title="Weather Prediction App", layout="centered")

st.title("🌦 Weather Prediction App")

data = pd.read_csv("data/data.csv")

st.subheader("📊 Dataset Preview")
st.dataframe(data)

st.subheader("📈 Temperature Trend")
plt.figure()
plt.plot(data['temperature'])
plt.xlabel("Index")
plt.ylabel("Temperature")
st.pyplot(plt)

st.subheader("🔮 Predict Temperature")

humidity = st.slider("Humidity", 0, 100, 50)
wind = st.slider("Wind Speed", 0, 50, 10)
pressure = st.slider("Pressure", 980, 1050, 1010)

if st.button("Predict"):
    result = predict_temp(humidity, wind, pressure)
    st.success(f"Predicted Temperature: {result:.2f} °C")