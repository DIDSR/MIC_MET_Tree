# tree/nodes/q6_multi_measurement.py

NODE = {
    "id": "Q6",
    "title": "Multi-Class Classification \u2013 Level of Measurement of class labels",
    "type": "question",
    "content_html": """
        <p style="color: #333; line-height: 1.6; margin-bottom: 1rem;">Based on your input, your multi-class classification task is based on a reference standard with negligible unreliability and variability, and returns a single label output for each input. To proceed with providing evaluation metrics/methods, we need further information regarding the level of measurement for classes involved in your task. Please refer to the question at the bottom to provide the necessary information.</p>
    """,
    "question_text": "What is the level of measurement of your label output?",
    "options": [
        {
            "label": "nominal (i.e., the outcome can be categorized but not ranked, e.g., classifying images into dog/cat/duck)",
            "next": "N1_4",
        },
        {
            "label": "ordinal (i.e., the outcome can be categorized and ranked, but the intervals between neighboring ranks may not be quantifiable, e.g., diagnosing patients as normal or mildly/moderately/severely diseased)",
            "next": "N1_5",
        },
    ],
}
