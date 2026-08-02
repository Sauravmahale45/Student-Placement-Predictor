import streamlit as st
import joblib

from streamlit_option_menu import option_menu
from views.analytics import analytics_page
# -------------------------------
# Import CSS Loader
# -------------------------------
from utils.load_css import load_css

# -------------------------------
# Import Pages
# -------------------------------
from views.home import home_page
from views.prediction import prediction_page
from views.analytics import analytics_page
from views.about import about_page
from views.contact import contact_page

# -------------------------------
# Streamlit Configuration
# -------------------------------
st.set_page_config(
    page_title="Student Placement AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Load CSS
# -------------------------------
load_css()

# -------------------------------
# Load Machine Learning Model
# -------------------------------

try:

    model = joblib.load("models/placement_model.pkl")

    scaler = joblib.load("models/scaler.pkl")

except Exception as e:

    st.error(f"Error Loading Model : {e}")

    st.stop()

# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.image("assets/images/logo.png",width=140)

    st.markdown("# Placement AI")

    selected = option_menu(

        menu_title="Navigation",

        options=[
            "Home",
            "Prediction",
            "Analytics",
            "About",
            "Contact"
        ],

        icons=[
            "house-fill",
            "cpu-fill",
            "bar-chart-fill",
            "info-circle-fill",
            "telephone-fill"
        ],

        menu_icon="list",

        default_index=0,
    )

# -------------------------------
# Navigation
# -------------------------------

if selected == "Home":

    home_page()

elif selected == "Prediction":

    prediction_page(model, scaler)

elif selected == "Analytics":

    analytics_page(model)

elif selected == "About":

    about_page()

elif selected == "Contact":

    contact_page()
