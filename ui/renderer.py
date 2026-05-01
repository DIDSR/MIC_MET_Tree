# ui/renderer.py

import streamlit as st


def render_node(node: dict, state) -> None:
    node_type = node["type"]
    if node_type == "question":
        _render_question(node, state)
    elif node_type == "content":
        _render_content(node)
    elif node_type == "metric_selector":
        _render_metric_selector(node, state)
    else:
        st.error(f"Unknown node type: {node_type}")


def _render_question(node, state):
    st.markdown(node["content_html"], unsafe_allow_html=True)
    st.markdown(
        f"<p style='font-size:1.125rem;font-weight:bold;margin-top:2rem;'>"
        f"{node['question_text']}</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='font-size:1.5rem;font-weight:600;margin-top:2rem;"
        "margin-bottom:1rem;'>Please select an option:</h3>",
        unsafe_allow_html=True,
    )
    for opt in node["options"]:
        btn_key = f"btn_{node['id']}_{opt['next']}"
        if st.button(opt["label"], key=btn_key):
            state["history"].append({
                "from": node["id"],
                "title": node["title"],
                "choice": opt["label"],
                "to": opt["next"],
            })
            state["current_node_id"] = opt["next"]
            state["selections"] = {}
            st.rerun()


def _render_content(node):
    st.markdown(node["content_html"], unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#666;margin-top:2rem;font-style:italic;text-align:center;">'
        '--- End of this branch. ---</p>',
        unsafe_allow_html=True,
    )


def _render_metric_selector(node, state):
    st.markdown(node["overview_html"], unsafe_allow_html=True)

    metrics = node["metrics"]
    options = ["--- Select a Metric ---"] + list(metrics.keys())
    sel_key = f"sel_{node['id']}"
    current = state["selections"].get(sel_key, options[0])
    if current not in options:
        current = options[0]

    chosen = st.selectbox(
        "Select a metric to learn more:",
        options,
        index=options.index(current),
        key=f"widget_{node['id']}",
    )
    state["selections"][sel_key] = chosen

    if chosen != options[0]:
        metric_data = metrics[chosen]
        st.subheader(f"Details for: {chosen}")
        st.markdown(metric_data["html"], unsafe_allow_html=True)
        if "sub_metrics" in metric_data:
            _render_sub_metric_selector(node, chosen, metric_data, state)
    else:
        st.info(
            "Choose a specific metric from the dropdown to see its "
            "definition, formulas, and references."
        )

    st.markdown(
        '<p style="color:#666;margin-top:2rem;font-style:italic;text-align:center;">'
        '--- End of this branch. ---</p>',
        unsafe_allow_html=True,
    )


def _render_sub_metric_selector(node, parent_metric, metric_data, state):
    sub_metrics = metric_data["sub_metrics"]
    sub_options = ["--- Select a Sub-Metric ---"] + list(sub_metrics.keys())
    sub_key = f"subsel_{node['id']}_{parent_metric}"
    current_sub = state["selections"].get(sub_key, sub_options[0])
    if current_sub not in sub_options:
        current_sub = sub_options[0]

    chosen_sub = st.selectbox(
        "Select a sub-metric:",
        sub_options,
        index=sub_options.index(current_sub),
        key=f"subwidget_{node['id']}_{parent_metric}",
    )
    state["selections"][sub_key] = chosen_sub

    if chosen_sub != sub_options[0]:
        sub_data = sub_metrics[chosen_sub]
        st.subheader(f"Details for: {chosen_sub}")
        st.markdown(sub_data["html"], unsafe_allow_html=True)
    else:
        st.info("Choose a specific sub-metric from the dropdown to see its details.")
