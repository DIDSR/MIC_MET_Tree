# Medical Imaging AI/ML Classification Metrics (MIC-MET) Decision Tree

## Overview

The Medical Imaging AI/ML Classification Metrics (MIC-MET) Decision Tree is a locally-hosted interactive web application developed in Python 
using the Streamlit framework, accessible through a web browser. The tool is designed to assist users in learning and exploring performance evaluation metrics and methods for AI/ML classification tasks in the medical imaging domain.

The tool guides users through a structured question-and-answer decision tree to
identify appropriate evaluation metrics based on their specific classification task
context, including:

- Type of classification task (binary or multi-class)
- Level of variability in the reference standard
- Type of AI/ML algorithm output

---

## Related Reference

Drukker K, Sahiner B, Hu T, Kim GH, Whitney HM, Baughan N, Myers KJ, Giger ML,
McNitt-Gray M. MIDRC-MetricTree: a decision tree-based tool for recommending
performance metrics in artificial intelligence-assisted medical image analysis.
*J Med Imaging.* 2024;11(2):024504.
doi: [10.1117/1.JMI.11.2.024504](https://doi.org/10.1117/1.JMI.11.2.024504).

## Disclaimer: Regulatory Science Tool (RST)

This tool serves as a Regulatory Science Tool (RST) and provides information and
resources concerning performance evaluation metrics and methods for AI/ML classification tasks in
the medical imaging domain. It is not intended to replace FDA-recognized standards
or FDA Medical Device Development Tools (MDDT).

This tool should not be interpreted as an FDA endorsement or recommendation for
specific metrics to be used in the evaluation of medical imaging AI/ML devices.

For more information about Regulatory Science Tools, visit:
https://www.fda.gov/medical-devices/science-and-research-medical-devices/catalog-regulatory-science-tools-help-assess-new-medical-devices

---

## Acknowledgements

We extend our special thanks to the Medical Imaging Data Resource Center (MIDRC)
TDP3c and TDP3d groups for their valuable contributions to this decision tree.

For a similar tree (MIDRC-MetricTree) designed for general AI/ML algorithm users,
visit: https://www.midrc.org/performance-metrics-decision-tree

The MIDRC-MetricTree was funded by the National Institute of Biomedical Imaging
and Bioengineering (NIBIB) of the National Institutes of Health under contracts
75N92020C00008 and 75N92020C00021.

---

## Requirements

- Python 3.8 or higher
- Streamlit

---

## Installation

**Step 1 — Clone or download this repository**

If using Git:

bash
git clone https://github.com/YOURUSERNAME/mic-met-classification.git
cd mic-met-classification


Or download the ZIP file from GitHub and unzip it.

**Step 2 — Install required packages**

bash
pip install -r requirements.txt


---

## How to Run the App

**Option 1 — Using standard Python:**
bash
"C:\Program Files\Python312\python.exe" -m streamlit run app.py


**Option 2 — If streamlit is on your system PATH:**
bash
streamlit run app.py


The app will open automatically in your default web browser at:
`http://localhost:8501`

---

## How to Use the App

1. **Start at the welcome page** — read the overview, acknowledgements, and disclaimers
2. **Answer the questions** — click the button that best describes your classification task
3. **Arrive at a metric page** — use the dropdown to explore individual metrics
4. **Navigate freely** — use the **Go Back** button to return to a previous question, or **Start Over** to begin again
5. **Review your path** — your navigation history is shown at the bottom of the page

---

## Folder Structure

mic-met-classification/
│
├── app.py                          ← Main entry point — run this to start the app
│
├── tree/                           ← Decision tree content
│   ├── registry.py                 ← Assembles all nodes into one lookup dictionary
│   └── nodes/                      ← One file per page of the decision tree
│       ├── q0welcome.py           ← Welcome / classification type question
│       ├── q1binaryrefstd.py     ← Binary: reference standard question
│       ├── q2binaryoutput.py     ← Binary: output type question
│       ├── q3multirefstd.py      ← Multi-class: reference standard question
│       ├── q4multioutput.py      ← Multi-class: output type question
│       ├── q5multilabels.py      ← Multi-class: number of labels question
│       ├── q6multimeasurement.py ← Multi-class: level of measurement question
│       ├── n01binarytruthvar.py ← Binary: truth variability metrics
│       ├── n02binary2x2.py       ← Binary: 2x2 confusion matrix metrics
│       ├── n03binarycurve.py     ← Binary: operating curve metrics
│       ├── n11multitruthvar.py  ← Multi-class: truth variability metrics
│       ├── n12multiscore.py      ← Multi-class: score output metrics
│       ├── n13multitopn.py       ← Multi-class: top-n accuracy metrics
│       ├── n14multikbyk.py       ← Multi-class: kxk confusion matrix metrics
│       └── n15multiordinal.py    ← Multi-class: ordinal classification metrics
│
├── ui/                             ← User interface rendering
│   ├── renderer.py                 ← Universal node renderer
│   ├── navigation.py               ← Back / Start Over buttons and history display
│   └── styles.py                   ← CSS styling
│
├── utils/                          ← Shared utilities
│   └── images.py                   ← Image loading helper
│
├── img/                            ← Static image assets
│   ├── G02binary2x2FigC.jpg
│   ├── G03binaryROCoverviewFig1300.jpg
│   ├── G03binaryAUROCFig1C.jpg
│   ├── G03binaryPartialAUROCFig1C.jpg
│   ├── G03binaryPRcurveFigC.jpg
│   ├── G03binaryareaunderPartialROCFig0C.jpg
│   ├── G03binaryareaunderPartialROCFig1C.jpg
│   ├── G12kClassscourOutputfigC.jpg
│   ├── G12kClassprobOutputfigC.jpg
│   ├── G13kClasstopnLabelfigC.jpg
│   ├── G13kClass1LabelfigC.jpg
│   ├── G14kClassordinalConfusionTabegfigC.jpg
│   ├── G15kClassordinalfigC.jpg
│   └── G15kClassordinalConfusionTabfigC.jpg
│
├── requirements.txt                ← Python package dependencies
├── .gitignore                      ← Files excluded from Git
└── README.md                       ← This file


---

## Adding a New Node (For Developers)

To add a new page to the decision tree:

1. Create a new file in `tree/nodes/` following the naming convention
2. Define a `NODE` dictionary with the required fields (`id`, `title`, `type`, and content)
3. Add one import line in `tree/registry.py`
4. Add the module to the `_ALL_NODES` list in `tree/registry.py`

No other files need to change.

---

## Contact

For questions about this tool, please contact Tingting.Hu@fda.hhs.gov.


