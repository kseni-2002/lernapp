import streamlit as st


def init_global_score():
    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    if "total_answered" not in st.session_state:
        st.session_state.total_answered = 0