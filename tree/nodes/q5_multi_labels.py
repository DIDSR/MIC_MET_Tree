# tree/nodes/q5_multi_labels.py

NODE = {
    "id": "Q5",
    "title": "Multi-Class Classification \u2013 Number of labels in output",
    "type": "question",
    "content_html": """
        <p style="color: #333; line-height: 1.6; margin-bottom: 1rem;">Based on your input, your multi-class classification task is based on a reference standard with negligible unreliability and variability, and label output. To proceed with providing evaluation metrics/methods, we need additional details regarding the number of labels in your output for each case. Please refer to the question at the bottom to provide the necessary information.</p>
    """,
    "question_text": "Does your output provide",
    "options": [
        {
            "label": "A single class label for each input (i.e., the most likely class)",
            "next": "Q6",
        },
        {
            "label": "Multiple class labels for each input (i.e., the n most likely classes, n>1)",
            "next": "N1_3",
        },
    ],
}
