import streamlit as st
from datetime import date, timedelta
import calendar

def calculate_age_details(birthdate):
    """Return (years, months, days) between birthdate and today."""
    today = date.today()

    if birthdate > today:
        raise ValueError("Birthdate is in the future")

    # Years
    years = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1

    # Months
    months = today.month - birthdate.month
    if today.day < birthdate.day:
        months -= 1
    months = months % 12  # normalize to 0-11

    # Days
    if today.day >= birthdate.day:
        days = today.day - birthdate.day
    else:
        # borrow days from previous month
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days = today.day + days_in_prev_month - birthdate.day

    return years, months, days

def days_until_next_birthday(birthdate):
    """Return days until next birthday from today (0 if today)."""
    today = date.today()
    this_year_bday = date(today.year, birthdate.month, birthdate.day)
    if this_year_bday < today:
        next_bday = date(today.year + 1, birthdate.month, birthdate.day)
    else:
        next_bday = this_year_bday
    return (next_bday - today).days

st.markdown("""
<div style='text-align:center;'>
    <span style='font-size:60px;'>🎂</span>
    <h1>Advanced Age Calculator</h1>
    <p style='font-size:16px;'>Shows Years, Months, and Days</p>
</div>
""", unsafe_allow_html=True)

birthdate = st.date_input("Select your date of birth")  # no fixed default; user must choose

if st.button("Calculate Age"):
    try:
        years, months, days = calculate_age_details(birthdate)
        st.success(f"You are {years} years, {months} months, and {days} days old.")
        # Extra helpful info
        total_days = (date.today() - birthdate).days
        st.info(f"Total days lived: {total_days} days.")
        days_to_bday = days_until_next_birthday(birthdate)
        if days_to_bday == 0:
            st.balloons()
            st.write("Happy Birthday! 🎉")
        else:
            st.write(f"Days until next birthday: {days_to_bday} day(s).")
    except ValueError as e:
        st.error(str(e))
