# tree/nodes/q0_welcome.py

NODE = {
    "id": "Q0",
    "title": "Classification",
    "type": "question",
    "content_html": """
        <section style="margin-bottom: 1.5rem;">
            <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Welcome to our classification branch.</h2>
            <p style="color: #333; line-height: 1.6;">Here we offer information resources on performance evaluation metrics and methods for AI/ML classification tasks. Before we proceed, it would be helpful to gather some context about your specific classification task. Please refer to the question at the bottom.</p>
        </section>
        <section style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Acknowledgement</h3>
            <p style="color: #333; line-height: 1.6;">We extend our special thanks to the Medical Imaging Data Resource Center (MIDRC) TDP3c and TDP3d groups for their valuable contributions to this decision tree. For a similar tree (MIDRC-MetricTree) designed for general AI/ML algorithm users, you can visit <a href="https://www.midrc.org/performance-metrics-decision-tree" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://www.midrc.org/performance-metrics-decision-tree</a>. The MIDRC-MetricTree was funded by the National Institute of Biomedical Imaging and Bioengineering (NIBIB) of the National Institutes of Health under contracts 75N92020C00008 and 75N92020C00021.</p>
        </section>
        <section style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Warning: Limited Scope of this Tool</h3>
            <p style="color: #333; line-height: 1.6;">This classification metric tool is designed to assist users in learning and exploring metrics commonly considered for medical imaging-based AI/ML classification tasks. However, it is crucial to keep the following limitations in mind while using this tool, and always exercise professional judgment when evaluating medical imaging devices.</p>
            <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
                <li>This tool should not be interpreted as an FDA endorsement or recommendation for specific metrics to be used in the evaluation of such devices.</li>
                <li>The sponsor knows their device the best, and an appropriate metric for their device may be something other than what is discussed as part of this tool.</li>
                <li>A single summary metric usually will not suffice when evaluating a device for safety and effectiveness. Typically, more than one metric and analysis is needed.</li>
                <li>Setting the performance goal for a metric that is clinically meaningful is just as important as choosing the metric, which is out of the scope of this tool.</li>
            </ul>
        </section>
        <section style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Disclaimer: Regulatory Science Tool (RST)</h3>
            <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
                <li>This tool serves as a Regulatory Science Tool (RST) and provides information and resources concerning performance evaluation metrics and methods for AI/ML classification tasks in the medical imaging domain. However, it is crucial to understand that an RST is not intended to replace FDA-recognized standards or FDA Medical Device Development Tools (MDDT).</li>
                <li>For marketing submissions, sponsors considering the use of this tool may request feedback or meetings for medical device submissions as part of the Q-Submission Program. This will help ensure compliance with the appropriate regulatory guidance and standards.</li>
            </ul>
            <p style="color: #333; line-height: 1.6;">For more comprehensive information about Regulatory Science Tools (RSTs) and their role in assessing new medical devices, please refer to the FDA's official website at <a href="https://www.fda.gov/medical-devices/science-and-research-medical-devices/catalog-regulatory-science-tools-help-assess-new-medical-devices" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://www.fda.gov/medical-devices/science-and-research-medical-devices/catalog-regulatory-science-tools-help-assess-new-medical-devices</a>.</p>
        </section>
    """,
    "question_text": "What best describes your clinical classification task?",
    "options": [
        {
            "label": "Binary classification - classification task with 2 classes (for example, classification of cases as diseased or not)",
            "next": "Q1",
        },
        {
            "label": "Multi-class classification - classification task with more than 2 classes (for example, classification of cases as 3 or more type of diseases)",
            "next": "Q3",
        },
    ],
}