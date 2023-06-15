import streamlit as st

st.title("Weather forecast for next few days...")

place = st.text_input("Enter the place for forecast :")

days = st.slider("Forecast Days :", min_value=1, max_value=5, help="select the number of days to view the forecast")

data = st.selectbox("Select data to View", ('Sky','Temperature'))

st.subheader(f"{data} for next {days} Days in {place} :")


