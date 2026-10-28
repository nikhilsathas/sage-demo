from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Sage | Equipment Finance", page_icon="🌿", layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>.block-container {padding-top: 1rem; padding-bottom: 0; max-width: 100%;}</style>", unsafe_allow_html=True)
st.iframe(Path(__file__).parent / "Sage_USFleet_Demo_v3.0.html", height=900)
