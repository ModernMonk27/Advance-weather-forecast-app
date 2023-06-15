import plotly.express
import streamlit as st
import plotly.express as px

st.title("Weather forecast for next few days...")

place = st.text_input("Enter the place for forecast :")

days = st.slider("Forecast Days :", min_value=1, max_value=5, help="select the number of days to view the forecast")

data = st.selectbox("Select data to View", ('Sky','Temperature'))

st.subheader(f"{data} for next {days} Days in {place} :")

def get_dates(days):
    temperature = [.1, 10, 15]
    dates = ["27-10-96", '27-11-96', '28-10-96']
    temperature = [days * i for i in temperature]
    return dates, temperature

d, t = get_dates(days)



figure = plotly.express.line(x=d, y=t ,labels={"x":"Dates","y":"Temperature (C)"})
st.plotly_chart(figure)
