
import streamlit as st
from orchestrator import orchestrator

st.set_page_config(layout="wide")
st.title("🚀 SentinelOps AI")

log = st.text_area("Paste log")

if st.button("Analyze"):
    res = orchestrator(log)

    st.write("### Plan", res["plan"])
    st.metric("Confidence", res["confidence"])
    st.metric("Risk", res["risk"])

    st.info(res["explanation"])

    st.write("### Fix", res.get("fix"))

    if res["execution"]=="success":
        st.success("Execution Success")
    else:
        st.error("Execution Failed")

    st.write("### Ticket", res["ticket"])

    st.write("### Timeline")
    for t in res["timeline"]:
        st.write(t)
