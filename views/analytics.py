import streamlit as st
import pandas as pd
import plotly.express as px


def analytics_page(model):

    st.markdown("""
    <div class="hero">

    <h1>📊 Model Analytics Dashboard</h1>

    <p style="font-size:20px;">

    Performance analysis of the trained
    Machine Learning model.

    </p>

    </div>

    """, unsafe_allow_html=True)

    st.write("")

    # --------------------------
    # KPI CARDS
    # --------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Accuracy", "86.67%")

    with col2:
        st.metric("Precision", "87%")

    with col3:
        st.metric("Recall", "86%")

    with col4:
        st.metric("F1 Score", "86%")

    st.divider()

    # --------------------------
    # Feature Importance
    # --------------------------

    st.subheader("⭐ Feature Importance")

    importance = pd.DataFrame({

        "Feature": [
            "CGPA",
            "IQ",
            "Profile Score"
        ],

        "Importance": model.feature_importances_

    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    fig = px.bar(

        importance,

        x="Importance",

        y="Feature",

        orientation="h",

        text="Importance",

        color="Importance",

        color_continuous_scale="Blues"

    )

    fig.update_layout(
        height=450,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # --------------------------
    # Dataset Summary
    # --------------------------

    st.subheader("📋 Dataset Summary")

    summary = pd.DataFrame({

        "Metric":[

            "Total Samples",

            "Training Samples",

            "Testing Samples",

            "Features"

        ],

        "Value":[

            300,

            240,

            60,

            3

        ]

    })

    st.dataframe(
        summary,
        use_container_width=True
    )

    st.divider()

    # --------------------------
    # About Model
    # --------------------------

    st.subheader("🤖 Model Information")

    st.info("""

Algorithm : Random Forest Classifier

Hyperparameter Tuning : Optuna

Scaling : StandardScaler

Target Variable : placed

Features Used :

• CGPA

• IQ

• Profile Score

""")