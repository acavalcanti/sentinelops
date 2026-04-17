import streamlit as st
from main import run

st.title("SentinelOps AI")

log = st.text_area("Log")

if st.button("Run"):
    result = run(log)

    st.subheader("Pipeline")
    st.json(result)