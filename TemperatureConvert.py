import streamlit as st

st.title("Temperature convertor")
temperature = st.slider('What is the temperature', -200, 200, 0)
convertTo = st.radio("To what unit you want to convert?", ('Farenheit','Celcius.'))
if (convertTo== "F" ):
    newTemp = (temperature*9/5)+32
    unit="F"
elif (convertTo == "C"):
    newTemp = (temperature-32)*5/9
    unit="C"
st.markdown("The converted temperature is **(:.2f)** degrees {}.format(newTemp, unit)")
