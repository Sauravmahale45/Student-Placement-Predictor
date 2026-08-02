import streamlit as st
import pandas as pd
from utils.report import generate_report
from utils.charts import (
    create_gauge,
    probability_chart,
    feature_importance
)


def prediction_page(model, scaler):

    # ============================
    # PAGE TITLE
    # ============================

    st.markdown("""
    <div class="hero">
        <h1>🎯 Placement Prediction</h1>
        <p style="font-size:20px;">
            Enter student details and let AI predict placement.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ============================
    # TWO COLUMN LAYOUT
    # ============================

    left, right = st.columns(
        [1, 1],
        gap="large"
    )

    # ============================
    # LEFT PANEL
    # ============================

    with left:

        st.markdown("""
        <div class="card">

        <h2>📋 Student Information</h2>

        <p>

        Adjust the values below and click
        Predict.

        </p>

        </div>
        """,unsafe_allow_html=True)

        cgpa = st.slider(

            "📚 CGPA",

            0.0,

            10.0,

            7.5,

        step=.1

    )

        iq = st.slider(

            "🧠 IQ",

            50,

            150,

            100

        )

        profile = st.slider(

            "💼 Profile Score",

            0,

            100,

            50

        )

        st.write("")

        predict_btn = st.button(
            "🚀 Predict Placement",
            use_container_width=True,
            type="primary"
        )

    # ============================
    # RIGHT PANEL
    # ============================

    with right:

        st.markdown("""
        <div class="card">
            <h2>📊 Prediction Result</h2>
            <br>
            Press the Predict button.
        </div>
        """, unsafe_allow_html=True)

    # ============================
    # PREDICTION
    # ============================

    if predict_btn:

        import time

        with st.spinner("AI Model is predicting..."):

            time.sleep(1)

            sample = pd.DataFrame(
                [[cgpa, iq, profile]],
                columns=[
                    "cgpa",
                    "iq",
                    "profile_score"
                ]
            )

            sample_scaled = scaler.transform(sample)

            prediction = model.predict(sample_scaled)

            # ============================
            # PROBABILITY
            # ============================

            if hasattr(model, "predict_proba"):
                probability = model.predict_proba(sample_scaled)
                placed_probability = probability[0][1] * 100
                not_probability = probability[0][0] * 100
            else:
                placed_probability = 100 if prediction[0] == 1 else 0
                not_probability = 100 - placed_probability

            result = "Placed" if prediction[0] == 1 else "Not Placed"

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            if prediction[0] == 1:
                st.success("🎉 Student is likely to be PLACED")
            else:
                st.error("❌ Student is NOT likely to be placed")

        with col2:

            confidence = (
                placed_probability
                if prediction[0] == 1
                else not_probability
            )

            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )

        st.write("")

        # ============================
        # PROBABILITY TABLE
        # ============================

        df = pd.DataFrame({
            "Result": [
                "Placed",
                "Not Placed"
            ],
            "Probability (%)": [
                round(placed_probability, 2),
                round(not_probability, 2)
            ]
        })

        st.subheader("📋 Prediction Probability")
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.write("")

        # ============================
        # GAUGE CHART
        # ============================

        st.subheader("📊 Placement Gauge")

        gauge = create_gauge(placed_probability)

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

        st.write("")

        # ============================
        # PROBABILITY CHART
        # ============================

        st.subheader("📈 Probability Comparison")

        chart = probability_chart(
            placed_probability,
            not_probability
        )

        st.plotly_chart(
            chart,
            use_container_width=True
        )

        st.write("")

        # ============================
        # FEATURE IMPORTANCE
        # ============================

        st.subheader("⭐ Feature Importance")

        importance = feature_importance(model)

        st.plotly_chart(
            importance,
            use_container_width=True
        )

        st.write("")

        # ============================
        # INPUT SUMMARY
        # ============================

        st.subheader("📝 Input Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric("CGPA", cgpa)
        c2.metric("IQ", iq)
        c3.metric("Profile Score", profile)

        st.write("")

        # ============================
        # DOWNLOAD REPORT
        # ============================

        st.subheader("📄 Download Prediction Report")

        pdf_file = generate_report(
            cgpa,
            iq,
            profile,
            result,
            placed_probability
        )

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="⬇ Download PDF Report",
                data=file,
                file_name="Placement_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )