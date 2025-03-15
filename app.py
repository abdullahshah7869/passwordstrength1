import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    # Password strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&]', password))

    # Calculate strength
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Strength feedback
    if criteria_met == 5:
        return "Strong", "green", 100
    elif criteria_met == 4:
        return "Medium", "orange", 75
    elif criteria_met == 3:
        return "Weak", "red", 50
    else:
        return "Very Weak", "red", 25

# Streamlit UI setup
st.set_page_config(page_title="Password Strength Checker", layout="centered")

# Header
st.title("Password Strength Checker")
st.markdown("Check your password strength instantly!")

# Input field for password
password = st.text_input("Enter your password:", type="password")

# If password is provided, check the strength
if password:
    # Call the function to get strength
    strength, color, progress = check_password_strength(password)

    # Display strength label with color
    st.markdown(f"**Password Strength**: <span style='color:{color};'>{strength}</span>", unsafe_allow_html=True)

    # Display progress bar
    st.progress(progress)

    # Display criteria (guidelines)
    st.subheader("Password Criteria:")
    criteria = {
        "At least 8 characters": len(password) >= 8,
        "At least one uppercase letter": bool(re.search(r'[A-Z]', password)),
        "At least one lowercase letter": bool(re.search(r'[a-z]', password)),
        "At least one number": bool(re.search(r'[0-9]', password)),
        "At least one special character (@$!%*?&)": bool(re.search(r'[@$!%*?&]', password))
    }

    for criterion, met in criteria.items():
        color = "green" if met else "red"
        st.markdown(f"- <span style='color:{color};'>{criterion}</span>", unsafe_allow_html=True)

# Reset functionality
if st.button("Reset"):
    st.experimental_rerun()
