import streamlit as st

def homepage():
    """Displays the home page."""
    st.title("Home Page")
    st.write("Welcome to the home page! 🎉")

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "1_Login"  # Redirect back to the login page

homepage()
