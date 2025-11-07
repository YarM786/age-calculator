import streamlit as st
from datetime import date

def calculate_age(birthdate):
    today = date.today()
    years = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1
    return years

st.markdown("""
<div style='text-align:center;'>
    <span style='font-size:60px;'>🎂</span>
    <h1>Age Calculator</h1>
    <p style='font-size:20px;'>by You</p>
</div>
""", unsafe_allow_html=True)

st.write("Enter your Date of Birth:")
birthdate = st.date_input("Select date", value=date())

if st.button("Calculate Age"):
    age = calculate_age(birthdate)
    st.success(f"Your age is {age} years.")


