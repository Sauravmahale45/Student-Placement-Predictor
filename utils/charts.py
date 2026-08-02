import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# ===================================================
# Gauge Chart
# ===================================================

def create_gauge(probability):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability,
            title={
                "text": "Placement Probability (%)",
                "font": {"size": 24}
            },
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#4F46E5"},
                "steps": [
                    {"range": [0, 40], "color": "#ff4b4b"},
                    {"range": [40, 70], "color": "#FFD700"},
                    {"range": [70, 100], "color": "#00C853"},
                ],
            }
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    return fig


# ===================================================
# Probability Bar Chart
# ===================================================

def probability_chart(placed, not_placed):

    df = pd.DataFrame({
        "Category": ["Placed", "Not Placed"],
        "Probability": [placed, not_placed]
    })

    fig = px.bar(
        df,
        x="Category",
        y="Probability",
        text="Probability"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    return fig


# ===================================================
# Feature Importance
# ===================================================

def feature_importance(model):

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
        ascending=True
    )

    fig = px.bar(

        importance,

        x="Importance",

        y="Feature",

        orientation="h",

        text="Importance"

    )

    fig.update_traces(
        texttemplate="%{text:.3f}"
    )

    fig.update_layout(

        height=350,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white")

    )

    return fig