import streamlit as st
import re

def check_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    score = sum([length, bool(upper), bool(lower), bool(digit), bool(special)])
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

st.title("Password Strength Meter")
password = st.text_input("Enter your password", type="password")
if password:
    strength = check_strength(password)
    st.subheader(f"Strength: {strength}")
