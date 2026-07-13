import os
import uuid
from pathlib import Path
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(cleaned_metadata, preprocessing_report, plots, insights, recommendations):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    REPORTS_DIR = BASE_DIR / "storage" / "reports"
    REPORTS_DIR.mkdir(
    parents=True,
    exist_ok=True
    )
    
    filename = f"{uuid.uuid4()}.pdf"
    pdf_path = REPORTS_DIR / filename
    doc = SimpleDocTemplate(str(pdf_path))
    styles = getSampleStyleSheet()
    
    story = []
    story.append(
        Paragraph("AI Business Analyst Report", styles["Title"])
        )
    story.append(
        Paragraph("Automatically generated using AI Business Analyst", styles["Normal"] )
        )
    _add_preprocessing_report(story, styles, preprocessing_report)
    _add_dataset_metadata(story, styles, cleaned_metadata)
    _add_plots(story, styles, plots)
    _add_insights(story, styles, insights)
    _add_recommendations(story, styles, recommendations)
    doc.build(story)
    
    return {
    "filename": filename,
    "path": str(pdf_path)
}
    
def _add_preprocessing_report(story, styles, preprocessing_report):

    story.append(
        Paragraph("Preprocessing Operations", styles["Heading1"])
    )

    operations = preprocessing_report.get("operations", [])

    for operation in operations:

        story.append(
            Paragraph(
                f"<b>Operation:</b> {operation['operation']}",
                styles["BodyText"]
            )
        )

        parameters = operation.get("parameters", {})

        for key, value in parameters.items():

            story.append(
                Paragraph(
                    f"• {key}: {value}",
                    styles["BodyText"]
                )
            )

        story.append(
            Paragraph("<br/>", styles["BodyText"])
        )
        
def _add_dataset_metadata(story, styles, cleaned_metadata):

    story.append(
        Paragraph("Dataset Summary", styles["Heading1"])
    )

    for key, value in cleaned_metadata.items():

        story.append(
            Paragraph(
                f"<b>{key}</b>: {value}",
                styles["BodyText"]
            )
        )

    story.append(
        Paragraph("<br/>", styles["BodyText"])
    )
def _add_plots(story, styles, plots):
    
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    story.append(
        Paragraph("Generated Visualizations", styles["Heading1"])
    )

    for plot in plots:
        image_path = BASE_DIR / plot["path"].lstrip("/")
        story.append(
            Paragraph(
                f"<b>{plot['title']}</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                plot["reason"],
                styles["BodyText"]
            )
        )

        story.append(
            Image(
                str(image_path),
                width=400,
                height=250
                )
        )

        story.append(
            Paragraph("<br/>", styles["BodyText"])
        )
        
def _add_insights(story, styles, insights):

    story.append(
        Paragraph("Business Insights", styles["Heading1"])
    )

    for insight in insights["insights"]:

        story.append(
            Paragraph(
                f"<b>{insight['title']}</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Description:</b> {insight['description']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Evidence:</b> {insight['evidence']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Importance:</b> {insight['importance']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph("<br/>", styles["BodyText"])
        )
        
def _add_recommendations(story, styles, recommendations):

    story.append(
        Paragraph("Business Recommendations", styles["Heading1"])
    )

    for recommendation in recommendations["recommendations"]:

        story.append(
            Paragraph(
                f"<b>{recommendation['title']}</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Recommendation:</b> {recommendation['recommendation']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Reason:</b> {recommendation['reason']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Business Impact:</b> {recommendation['expected_impact']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Priority:</b> {recommendation['priority']}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph("<br/>", styles["BodyText"])
        )