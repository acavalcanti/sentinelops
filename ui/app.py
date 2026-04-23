import streamlit as st
import json
import pandas as pd

from orchestrator.pipeline import run_pipeline

st.set_page_config(page_title="SentinelOps AI", layout="wide")

st.title("SentinelOps AI - Multi-Agent Incident Advisor")

# 🧠 INPUT
log = st.text_area("Enter log", height=150)

# 🧠 SESSION STATE
if "state" not in st.session_state:
    st.session_state.state = None

# 🧪 QUICK SCENARIOS
st.subheader("Quick Test Scenarios")

col_q1, col_q2 = st.columns(2)

with col_q1:
    if st.button("OOM Error"):
        st.session_state.state = run_pipeline({
            "log": "ERROR: OutOfMemoryError container restart loop in order-service"
        })

with col_q2:
    if st.button("CrashLoopBackOff"):
        st.session_state.state = run_pipeline({
            "log": "ERROR: CrashLoopBackOff in payment-service"
        })

# 🧠 EXECUÇÃO MANUAL
if st.button("Run Analysis"):
    if log.strip():
        st.session_state.state = run_pipeline({"log": log})
    else:
        st.warning("Please enter a log before running analysis.")

# 🧠 RECUPERA STATE
state = st.session_state.state

if state is None:
    st.stop()

# 🧠 VALORES PRINCIPAIS (SEM FALLBACK PERIGOSO)
arbiter = state.get("arbiter_decision")
final_conf = state.get("final_confidence", 0)
decision_conf = state.get("decision_confidence", 0)

# 🟢 🔴 STATUS GLOBAL
if arbiter == "proceed":
    st.success(f"✅ Action Approved (arbiter confidence: {round(final_conf, 2)})")
elif arbiter == "review":
    st.warning(f"⚠️ Action Requires Review (arbiter confidence: {round(final_conf, 2)})")
else:
    st.error(f"⛔ Action Blocked (arbiter confidence: {round(final_conf, 2)})")

# 🧠 DECISION CONTEXT (🔥 importante para narrativa)
st.subheader("Decision Context")

policy = state.get("policy_result", {})
risk = policy.get("risk", "unknown")

if arbiter == "proceed":
    arbiter_msg = "High confidence → safe to proceed"
elif arbiter == "review":
    arbiter_msg = "Low confidence → human review required"
else:
    arbiter_msg = "Blocked by governance"

st.write({
    "Policy": f"Approved: {policy.get('approved')} (risk: {risk})",
    "Arbiter": arbiter_msg
})

# 📊 CONFIDENCE OVERVIEW (SEM FALLBACK)
st.subheader("Confidence Overview")

st.progress(final_conf)

col_c1, col_c2 = st.columns(2)

with col_c1:
    st.metric("Final Confidence (Arbiter)", round(final_conf, 3))

with col_c2:
    st.metric("Decision Confidence (Agent)", round(decision_conf, 3))

# 🧠 EXPLAINABILITY
st.subheader("Why this decision?")

st.write({
    "Analysis (LLM)": state.get("analysis_confidence"),
    "RAG (Knowledge)": state.get("rag_confidence"),
    "Decision (Agent)": decision_conf,
})

# 🧠 LAYOUT PRINCIPAL
col1, col2 = st.columns([2, 1])

# 🔍 COLUNA PRINCIPAL
with col1:

    st.subheader("Analysis")

    st.write(state.get("analysis", "N/A"))
    st.metric("Analysis Confidence", state.get("analysis_confidence", 0))

    st.subheader("Decision")

    decision = state.get("decision") or state.get("action_spec")

    if decision:
        st.json(decision)
    else:
        st.warning("No decision generated")

    st.subheader("Execution Result")
    st.json(state.get("execution_result", {}))

# 📊 COLUNA LATERAL
with col2:

    st.subheader("RAG (Retrieved Knowledge)")

    rag_data = state.get("rag_candidates", [])
    if rag_data:
        df = pd.DataFrame(rag_data)
        st.dataframe(df)
    else:
        st.info("No RAG candidates")

    st.metric("RAG Confidence", state.get("rag_confidence", 0))

    st.subheader("Arbiter Details")

    st.write("Decision:", arbiter)
    st.metric("Final Confidence", round(final_conf, 3))

    st.subheader("Policy")
    st.json(policy)

# 📈 METRICS
st.subheader("Outcome Evaluation")

metrics = state.get("metrics")

if metrics:
    st.json(metrics)
else:
    st.info("No evaluation available")

# 🔍 TRACE
with st.expander("🔍 Full State Debug"):
    st.json(state)

# 📥 EXPORT
if "trace" in state:

    trace_json = json.dumps(state["trace"], indent=2)

    st.download_button(
        label="📥 Export Audit Log",
        data=trace_json,
        file_name="sentinelops_audit.json",
        mime="application/json"
    )