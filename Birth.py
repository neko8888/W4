import streamlit as st
import datetime

st.title("Age in Days calculator")

today = datetime.date.today()
oldest = datetime.datetime(1900, 1, 1)

birth = st.date_input(
    "What is your date of birth?",
    today, min_value=oldest)

difference = today - birth

st.write("You are {} days old".format(difference.days))