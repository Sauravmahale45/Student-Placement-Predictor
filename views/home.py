import streamlit as st


def home_page():

    # -------------------------
    # Hero Section
    # -------------------------

    col1, col2 = st.columns([2,1])

    with col1:

        st.markdown("""

    <div class="hero">

    <h1>🎓 Student Placement Prediction</h1>

    <h3>

    AI Powered Placement Prediction Dashboard

    </h3>

    <br>

    Predict whether a student will get placed

    using Artificial Intelligence.

    </div>

    """,unsafe_allow_html=True)

    with col2:

        st.image(
            "assets/images/hero.png",
            use_container_width=True
        )
    # -------------------------
    # KPI Cards
    # -------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">
        <h2>🎯 Accuracy</h2>
        <h1>86.67%</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
        <h2>🤖 Algorithm</h2>
        <h1>Random Forest</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="card">
        <h2>📊 Features</h2>
        <h1>3</h1>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # -------------------------
    # About Section
    # -------------------------

    left, right = st.columns([2, 1])

    with left:

        st.markdown("""
        <div class="card">

        <h2>📌 About Project</h2>

        <p>

        This project predicts whether a student
        is likely to get placed based on
        academic and aptitude-related features.

        The prediction is made using a
        Random Forest Machine Learning model
        optimized with Optuna.

        </p>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("""
        <div class="card">

        <h2>🛠 Technology</h2>

        ✔ Python<br>
        ✔ Streamlit<br>
        ✔ Scikit-Learn<br>
        ✔ Plotly<br>
        ✔ Machine Learning<br>

        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # -------------------------
    # Features Section
    # -------------------------

    st.subheader("🚀 Application Features")

    feature1, feature2, feature3 = st.columns(3)

    with feature1:
        st.info("🎯 Predict Placement")

    with feature2:
        st.info("📊 Interactive Dashboard")

    with feature3:
        st.info("📈 ML Powered Decision")

    st.write("")
    st.write("")

    # -------------------------
    # Footer
    # -------------------------

    st.markdown("---")

    st.caption("Developed using ❤️ Python, Streamlit and Machine Learning")