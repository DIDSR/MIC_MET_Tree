# ui/navigation.py

import streamlit as st


def render_navigation(state) -> None:
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Start Over", key="start_over_btn"):
            state["current_node_id"] = "Q0"
            state["history"] = []
            state["selections"] = {}
            st.rerun()

    with col2:
        if state["history"]:
            if st.button("Go Back", key="go_back_btn"):
                last_step = state["history"].pop()
                state["current_node_id"] = last_step["from"]
                st.rerun()


def render_history(state) -> None:
    if state["history"]:
        st.markdown("---")
        st.markdown(
            "<h3 style='font-size:1.5rem;font-weight:600;margin-top:2rem;"
            "margin-bottom:1rem;'>Your Navigation History:</h3>",
            unsafe_allow_html=True,
        )
        for i, entry in enumerate(state["history"]):
            st.markdown(
                f"**Step {i + 1}:** From '{entry['title']}' "
                f"you chose: {entry['choice']}"
            )
