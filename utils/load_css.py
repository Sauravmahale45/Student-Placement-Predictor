import streamlit as st

def load_css():
    with open("assets/css/style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )