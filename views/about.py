import streamlit as st


def about_page():

    # =====================================
    # HERO SECTION
    # =====================================

    st.markdown("""
    <div class="hero">

    <h1>📖 About This Project</h1>

    <h3>
    AI Powered Student Placement Prediction
    </h3>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # =====================================
    # PROJECT OVERVIEW
    # =====================================

    left, right = st.columns([2,1])

    with left:

        st.markdown("""
        <div class="card">

        <h2>🎯 Project Overview</h2>

        <p>

        Student Placement Prediction is an
        Artificial Intelligence application
        developed using Machine Learning.

        It predicts whether a student
        is likely to get placed based on

        • CGPA

        • IQ

        • Profile Score

        The application uses a trained
        Random Forest Classifier model.

        </p>

        </div>

        """, unsafe_allow_html=True)

    with right:

        st.markdown("""
        <div class="card">

        <h2>🛠 Tech Stack</h2>

        ✅ Python

        <br>

        ✅ Streamlit

        <br>

        ✅ Scikit-Learn

        <br>

        ✅ Plotly

        <br>

        ✅ Pandas

        <br>

        ✅ NumPy

        </div>

        """, unsafe_allow_html=True)

    st.write("")

    # =====================================
    # MACHINE LEARNING PIPELINE
    # =====================================

    st.subheader("🧠 Machine Learning Workflow")

    st.markdown("""

1️⃣ Data Collection

⬇

2️⃣ Data Cleaning

⬇

3️⃣ Exploratory Data Analysis (EDA)

⬇

4️⃣ Feature Engineering

⬇

5️⃣ Model Training

⬇

6️⃣ Hyperparameter Tuning

⬇

7️⃣ Model Evaluation

⬇

8️⃣ Deployment using Streamlit

""")

    st.divider()

    # =====================================
    # DATASET INFORMATION
    # =====================================

    st.subheader("📊 Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric("Samples", "300")

    with col2:

        st.metric("Features", "3")

    with col3:

        st.metric("Target", "Placed")

    st.divider()

    # =====================================
    # MODEL INFORMATION
    # =====================================

    st.subheader("🤖 Model Information")

    st.success("""

Algorithm : Random Forest Classifier

Hyperparameter Tuning : Optuna

Feature Scaling : StandardScaler

Prediction Type : Binary Classification

""")

    st.divider()

    # =====================================
    # FUTURE ENHANCEMENTS
    # =====================================

    st.subheader("🚀 Future Enhancements")

    st.info("""

• Student Resume Analysis

• Interview Performance Prediction

• Placement Recommendation

• Company Recommendation

• Salary Prediction

• AI Career Guidance

""")

    st.divider()

    # =====================================
    # DEVELOPER
    # =====================================

    st.subheader("👨‍💻 Developer")

    st.markdown("""

**Name :** Your Name

**Project :** Student Placement Prediction

**Technology :** Python | Streamlit | Machine Learning

""")

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "🌐 GitHub",
            "https://github.com/"
        )

    with col2:

        st.link_button(
            "💼 LinkedIn",
            "https://linkedin.com/"
        )