from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

import datetime


def generate_report(
        cgpa,
        iq,
        profile,
        prediction,
        confidence):

    filename = "Placement_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>Student Placement Prediction Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"Date : {datetime.datetime.now()}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>CGPA :</b> {cgpa}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>IQ :</b> {iq}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Profile Score :</b> {profile}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            f"<b>Prediction :</b> {prediction}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Confidence :</b> {confidence:.2f} %",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "Prediction generated using Random Forest Machine Learning Model.",
            styles["Italic"]
        )
    )

    doc.build(story)

    return filename