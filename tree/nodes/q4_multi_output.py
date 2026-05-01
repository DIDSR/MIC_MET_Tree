# tree/nodes/q4_multi_output.py

NODE = {
    "id": "Q4",
    "title": "Multi-Class Classification \u2013 Type of AI/ML algorithm output",
    "type": "question",
    "content_html": """
        <p style="color: #333; line-height: 1.6; margin-bottom: 1rem;">Based on the information provided, your <i>multi-class</i> classification task is based on <i>reference standard with negligible unreliability and variability</i>. To proceed with providing evaluation metrics/methods, we need additional details regarding the type of output in your classification task. Please refer to the question at the bottom to provide the necessary information.</p>
    """,
    "question_text": "What is the output of your AI/ML algorithm?",
    "options": [
        {
            "label": "Score output (A score output indicates a numerical score representing how much likely the case belongs to a class)",
            "next": "N1_2",
        },
        {
            "label": "Label output (A label output indicates one or more of the classes (e.g., categorical variables) the case most likely belongs to)",
            "next": "Q5",
        },
    ],
}
