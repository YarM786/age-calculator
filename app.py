```python
# app.py
import streamlit as st
from datetime import date

def calculate_age_details(birthdate):
    today = date.today()

    # Years
    years = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1

    # Calculate months
    months = today.month - birthdate.month
    if today.day < birthdate.day:
        months -= 1
    if months < 0:
        months += 12

    # Calculate days
    if today.day >= birthdate.day:
        days = today.day - birthdate.day
    else:
        import calendar
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days = today.day + days_in_prev_month - birthdate.day

    return years, months, days

st.markdown("""
<div style='text-align:center;'>
    <span style='font-size:60px;'>🎂</span>
    <h1>Advanced Age Calculator</h1>
    <p style='font-size:20px;'>Shows Years, Months, and Days</p>
</div>
""", unsafe_allow_html=True)

birthdate = st.date_input("Select your date of birth")

if st.button("Calculate Age"):
    years, months, days = calculate_age_details(birthdate)
    st.success(f"You are {years} years, {months} months, and {days} days old.")
```

```
# requirements.txt
streamlit
```
