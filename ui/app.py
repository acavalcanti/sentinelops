import streamlit as st
import json
import time

from orchestrator.pipeline import run_pipeline
from llm.providers.ollama import stream_generate
from core.config import CONFIG

st.set_page_config(layout="wide")
st.title("🧠 SentinelOps AI — Glass Box Demo")

# INPUT
log = st.text_area(
    "Incident Log",
    "ERROR: OutOfMemoryError container restart loop in order-service"
)

if st.button("Run Analysis"):

    state = run_pipeline({"log": log})

    col1, col2 = st.columns([2, 1])

    if "trace" in state:
        st.download_button(
            "Export Audit Log",
            json.dumps(state["trace"], indent=2),
            "audit_log.json"
        )

    # =========================
    # LEFT — REASONING
    # =========================
    with col1:

        st.header("🧠 AI Reasoning")

        # 🔥 NOVO — explicação da confiança (sem hardcode)
        st.caption(CONFIG["ui"]["confidence_note"])

        # -------------------------
        # ANALYSIS
        # -------------------------
        with st.expander("📌 Analysis", expanded=True):

            analysis = state.get("analysis")

            if analysis:
                st.markdown(analysis)
            else:
                container = st.empty()
                text = ""

                try:
                    for token in stream_generate(log, CONFIG):
                        text += token
                        container.markdown(text)
                except Exception:
                    st.warning("No analysis available")

            st.metric(
                "Confidence",
                float(state.get("analysis_confidence", 0))
            )

        # -------------------------
        # RAG
        # -------------------------
        with st.expander("📚 RAG Retrieval", expanded=True):

            candidates = state.get("rag_candidates", [])

            if candidates:
                for c in candidates:
                    st.write(c.get("action"))
                    st.progress(float(c.get("score", 0)))
            else:
                st.info("No candidates")

            st.metric(
                "RAG Confidence",
                float(state.get("rag_confidence", 0))
            )

        # -------------------------
        # DECISION
        # -------------------------
        with st.expander("🎯 Decision", expanded=True):
            st.json(state.get("decision", {}))

        # -------------------------
        # CONFIDENCE BREAKDOWN
        # -------------------------
        with st.expander("📊 Confidence Breakdown", expanded=True):

            st.bar_chart({
                "analysis": float(state.get("analysis_confidence", 0)),
                "rag": float(state.get("rag_confidence", 0)),
                "decision": float(state.get("decision_confidence", 0)),
                "final": float(state.get("final_confidence", 0))
            })

            st.metric(
                "Final Confidence",
                float(state.get("final_confidence", 0))
            )

    # =========================
    # RIGHT — GOVERNANCE
    # =========================
    with col2:

        st.header("🛡️ Governance")

        arbiter = state.get("arbiter_decision")

        if arbiter == "halt":
            st.error("HALT")
        elif arbiter == "review":
            st.warning("REVIEW")
        else:
            st.success("PROCEED")

        st.metric("Decision", arbiter)

        # 🔥 NOVO — explicação do arbiter (sem hardcode)
        st.caption(CONFIG["ui"]["arbiter_label"])
        st.write(state.get("arbiter_reason", CONFIG["ui"]["arbiter_default"]))

        st.divider()

        # -------------------------
        # PIPELINE FLOW
        # -------------------------
        st.header("🧠 Pipeline Flow")

        for step, key in [
            ("Analysis", "analysis_confidence"),
            ("RAG", "rag_confidence"),
            ("Decision", "decision_confidence"),
            ("Arbiter", "final_confidence")
        ]:
            st.write(step)
            st.progress(float(state.get(key, 0)))
            time.sleep(CONFIG["ui"]["flow_delay"])

        st.divider()

        # -------------------------
        # EXECUTION
        # -------------------------
        st.header("⚙️ Execution")

        execution = state.get("execution_result")

        if isinstance(execution, dict):
            st.json(execution)
        else:
            st.info(CONFIG["ui"]["execution_empty"])

    # =========================
    # METRICS
    # =========================
    st.header("📊 Outcome Evaluation")

    metrics = state.get("metrics")

    if metrics:
        st.json(metrics)
    else:
        st.info(CONFIG["ui"]["metrics_empty"])

    # =========================
    # HISTORY
    # =========================
    st.header("📈 History")

    try:
        with open(CONFIG["history"]["file"]) as f:
            history = json.load(f)
    except Exception:
        history = []

    if history:
        scores = [
            float(h.get("metrics", {}).get("score", 0))
            for h in history
        ]

        st.line_chart(scores)

    # =========================
    # DEBUG
    # =========================
    with st.expander("🔎 Full State Debug"):
        st.json(state)