# app.py

import streamlit as st
from tree.registry import QA_TREE
from ui.styles import CSS
from ui.renderer import render_node
from ui.navigation import render_navigation, render_history

# --- Page config ---
st.set_page_config(
    layout="centered",
    page_title="Medical Imaging AI/ML Classification Metrics (MIC-MET) Decision Tree"
)
st.markdown(CSS, unsafe_allow_html=True)
st.title("Medical Imaging AI/ML Classification Metrics (MIC-MET) Decision Tree")


# --- Initialize session state ---
if "current_node_id" not in st.session_state:
    st.session_state["current_node_id"] = "Q0"
if "history" not in st.session_state:
    st.session_state["history"] = []
if "selections" not in st.session_state:
    st.session_state["selections"] = {}

state = st.session_state

# --- Look up current node ---
current_node = QA_TREE[state["current_node_id"]]

# --- Display node title ---
st.markdown(
    f'<h2 style="font-size:2.25rem;font-weight:bold;color:#2c5282;'
    f'text-align:center;margin-bottom:1.5rem;">'
    f'{current_node["title"]}</h2>',
    unsafe_allow_html=True,
)

# --- Render node content ---
render_node(current_node, state)

# --- Render navigation buttons and history ---
render_navigation(state)
render_history(state)
