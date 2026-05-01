# tree/nodes/q1_binary_refstd.py

NODE = {
    "id": "Q1",
    "title": "Binary classification \u2013 Reference Standard",
    "type": "question",
    "content_html": """
        <section style="margin-bottom: 1.5rem;">
            <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Overview</h2>
            <p style="color: #333; line-height: 1.6;">You have identified your task as a <i>binary classification</i> task. To provide you with relevant information resources on performance evaluation metrics for your task, we need to understand the level of variability in your reference standard (i.e., ground truth). Please answer the question at the bottom and select the option that best describes your task.</p>
        </section>
        <section style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Related Concepts</h3>
            <p style="color: #333; line-height: 1.6;">In this branch, we adopt the definition of 'reference standard' given by STARD (Cohen et al., 2016): "<i>Clinical reference standard</i> is the best available method for establishing the presence or absence of the target condition. A <i>gold standard</i> would be an error-free reference standard." Note that the reference standard definition used here is for diagnostic accuracy studies, and thus may not apply to other problems/task settings.</p>
        </section>
    """,
    "question_text": "Does your reference standard, or \u201ctruth\u201d, have negligible unreliability and variability?",
    "options": [
        {
            "label": "Negligible unreliability and variability in reference standard (There is a high certainty that the labels are reliable and the truthing process will yield the same labels for all cases when repeated, accurate on average)",
            "next": "Q2",
        },
        {
            "label": "Non-Negligible unreliability and variability in reference standard (There is substantial deterministic error or variability in the truth, e.g., because it relies on human determination)",
            "next": "N0_1",
        },
    ],
}