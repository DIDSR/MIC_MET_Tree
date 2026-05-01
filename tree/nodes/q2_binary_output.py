# tree/nodes/q2_binary_output.py

NODE = {
    "id": "Q2",
    "title": "Binary classification \u2013 Output Type",
    "type": "question",
    "content_html": """
        <p style="color: #333; line-height: 1.6; margin-bottom: 1rem;">Based on the information provided, the reference standard you used in your classification task exhibits negligible unreliability and variability. To proceed with providing evaluation metrics/methods, we need additional details regarding the type of output in your classification task. Please refer to the question at the bottom to provide the necessary information.</p>
    """,
    "question_text": "What is the type of output of your AI/ML algorithm?",
    "options": [
        {
            "label": "Binary (2-class) output (e.g. disease present / disease absent)",
            "next": "N0_2",
        },
        {
            "label": "Non-binary output (e.g. continuous (such as a probability of disease) or ordinal (such as a severity rating))",
            "next": "N0_3",
        },
    ],
}
