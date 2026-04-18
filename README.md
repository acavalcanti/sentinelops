# SentinelOps AI

## Overview

SentinelOps AI is a Glass-Box AI Ops demo platform designed to demonstrate how an enterprise-grade incident analysis and remediation system can be built using:

- Multi-agent orchestration
- Retrieval-Augmented Generation (RAG)
- Policy-based governance
- Safe execution abstraction (MCP)

This project prioritizes:

Explainability over autonomy
Correct architecture over production scale
Demonstration clarity over complexity

---

## Purpose of this Demo

This project was built to demonstrate:

- How to design AI systems beyond simple LLM calls
- How to introduce governance and safety into AI decisions
- How to integrate AI with enterprise platforms like OpenShift
- How to separate reasoning (AI) from execution (systems)

---

## Key Concepts Demonstrated

- AI Orchestration (LangGraph)
- RAG with vector databases (Qdrant)
- Model abstraction (LLM Router)
- Policy-based decision control
- Human-in-the-loop readiness
- Cloud-native deployment

---

## Architecture

### High-Level Flow

Log → Analysis → Signature → RAG → Decision → Arbiter → Policy → Execution → Learning

---

### Architectural Principles

- AI does not execute actions directly
- All execution passes through policy validation
- Decisions are explainable and traceable
- Models are decoupled from orchestration

---

## Why These Technologies

| Component | Reason |
|----------|--------|
| LangGraph | Structured agent orchestration |
| Qdrant | Lightweight vector DB |
| Streamlit | Fast UI for explainability |
| Podman | OpenShift-aligned container runtime |
| OpenShift AI | Enterprise model serving |

---

## Local Setup

### Requirements

- Python 3.10+
- Podman
- podman-compose
- Ollama

### Run services

podman compose -f infra/podman-compose.yaml up

### Mac user might need to run this steps to create a virtual environment

python3 -m venv .venv
source .venv/bin/activate

### Install dependencies

pip install -r requirements.txt

### Initialize RAG

python -c "from rag.setup import init_qdrant; init_qdrant()"

### Install Ollama

brew install ollama

### Start Ollama server

ollama serve

### Pull a lightweight model (RECOMMENDED)

ollama pull phi

### Test model

ollama run phi

If the model responds, setup is correct.

### Run app

streamlit run ui/app.py

---

## OpenShift Deployment

### Requirements

- OpenShift 4.18+
- OpenShift AI 2.x+

### Steps

1. Build image with Podman
2. Push to registry
3. Deploy using `oc`
4. Configure ConfigMap
5. Expose route

---

## OpenShift AI Integration

The system supports external model serving via OpenShift AI.

To enable:

- Deploy model using vLLM runtime
- Update config.yaml with endpoint
- Switch provider to "openshift"

---

## Extending the System

### Adding a new model

- Create provider in `llm/providers/`
- Register in router

---

### Adding a new tool

- Add to `tools.yaml`
- Implement handler in MCP layer

---

### Adding new signatures

- Update `signatures.yaml`

---

## Future Improvements

- Ansible Automation Platform integration
- Kafka event-driven pipeline
- Multi-model consensus
- Advanced observability
- Policy engine externalization

---

## Demo Value

This project demonstrates a transition from:

- AI toy examples → real systems
- LLM usage → AI architecture
- scripts → platforms
