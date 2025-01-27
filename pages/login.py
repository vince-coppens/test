import streamlit as st

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"

def login():
    """Displays the login screen and handles login logic."""
    st.title("Login Page")

    # Login form
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.experimental_
            #st.session_state.page = "2_Homepage"  # Redirect to the home page
            st.success("Login successful! Redirecting...")
        else:
            st.error("Invalid username or password.")

login()