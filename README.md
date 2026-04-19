# SentinelOps AI

## Overview

SentinelOps AI is a **Glass-Box AI Ops demo platform** designed to demonstrate how to build **governed, explainable, multi-agent AI systems** for incident response in cloud-native environments.

This is **not a production system** — it is an **architecture-first demo** focused on:

* Explainability over autonomy
* Governance over blind execution
* System design over feature completeness

---

## 🧠 Architecture First Approach

📄 **Full architecture and design rationale:**
➡️ See [`ARCHITECTURE.md`](./ARCHITECTURE.md)

This document explains:

* Why each layer exists
* Tradeoffs (LangGraph, Qdrant, YAML policy)
* Separation between probabilistic vs deterministic logic
* Governance and risk mitigation strategy

---

## 🎯 Purpose of this Demo

This project demonstrates:

* How to design **AI systems beyond simple LLM calls**
* How to implement **governance layers for AI safety**
* How to separate:

  * **Reasoning (LLMs)**
  * **Control (Policy / Arbiter)**
  * **Execution (Systems)**
* How to build **trustable AI systems** instead of black-box automation

---

## 🧩 Core Concepts Demonstrated

* Multi-Agent Orchestration (LangGraph)
* Retrieval-Augmented Generation (Qdrant)
* Model Abstraction (LLM Router)
* Policy-as-Code (YAML-driven governance)
* Human-in-the-Loop readiness
* Glass-Box Explainability UI

---

## 🔁 System Flow

```text
Log → Analysis → Signature → RAG → Decision → Arbiter → Policy → Execution → Evaluation
```

---

## 🧠 Key Architectural Principle

> The LLM is treated as an **unreliable component** — and is governed accordingly.

* LLM generates hypotheses
* RAG adds context
* Decision proposes action
* Arbiter evaluates confidence
* Policy validates safety
* Execution is isolated

---

## 🖥️ Glass-Box UI (Core Differentiator)

### 🧠 AI Reasoning + RAG + Decision

![Image](https://images.openai.com/static-rsc-4/-jlk5V3Gfq_hnnVlar26kxJTTN9fllotGrxStSpnCBlTdnqfUgg1CvsKmSg_lwtBpp3yGJsoo4BT5IXViLjZSXBbSPNb1tCx9mjPH1F38PCdORfP9XyEti9NrK29WGEoe-NqAkoNVlPXcUtyJ7N_KnWjkI1q-MV_e0et99U0WgJeDBXQ91P-4-Ub6IgNN9qK?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/5ILzyRd4J8sDJE6QCWRF-YovVeyj--LJ4zT1RlqKG6Ldk13lsxnWiWTXGYxrrAa7BFp5uEyjq0oXEljL9vVBZEvdDsLU904FPKuv3QmjcVQ2dV30vWYg28EcjJOZjkndsae2AP7J0A1Z_eXHO7QaqgqRJVWhx50g89Mx4WcwSPND25VfT3dUS19d8Htqki2o?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/nRaNS2FoeqjFW9mi4W1YIaHSfcarZHbavSzDf8S8euYnYDQGU9DbnqDpAiHATL7tF9-z1Vy18BYHqZxagdRgWp4BnT6Tnwfpwd8FXgn-2R5OcPQrIEds6yL0kUwUnK6n9SzgFVpBxyAyxEKWNovolGxeMz7UborvMKkTKSxQe7vWiJ6BeRUBtFkVqcEGvWfk?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/V5RZZ__OhS3pMDqjN3H6A5LIi261Y8U6OIU8yW-g88bDfx7N1IgkiWSMDWtjBMPy17iju5cO9P-faqzSg8pYPl6ki76R7SOOBlQIHpLx3JfbEMrDBPyhijSyw-hWSvn_KwBoe8-BXlfUclacOvLz7eghuKgbWvuOhR6-nz8nwzvr9DHtLO5bpgHymgLgn2go?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/NYpTaMzNuaV9EEiwlbB-R3BN_Yvcb6ZEGKWWBLzz4tOTkWW_nNmgUt5uoHwaROgxjtFBa-IvJ_YoTOHFezpZ9GxgeaKcgq8PJ5ivK85PpXg12RUx96QwIi7RhHT_LLAuS_iqhdW7afUcDSzXiXHSHokvCgvNY2Mf-Fpwbe6S7VahcBPL_dPQ7ZazMDwTNupr?purpose=fullsize)

The UI exposes:

* Full reasoning trace
* RAG retrieval candidates
* Decision structure
* Confidence breakdown

---

### 🛡️ Governance + Pipeline Flow + Execution

![Image](https://images.openai.com/static-rsc-4/3w6v4rzwSKqCa1RdiVvyn-sR_gM0ATDDLGQCiU4vm-CEZlA7cB58E47muZQLCBH8LXfdIJdRtM7i_NQThuMTtZJt5xHHYPTePuwoXKHglSJ4yvTQIe6uxrS_AZkUNW-3S3pkGBp1GcsgVasLiRkcfUv2VOXy5VKYwVTtNyWTEQSpHp3oHes_IQhdYT0yzY_k?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/1j6hwDdHrdquUEU_YK4VDobPtlrIXsg8R_y3JU_RckC9cHB0bAsrPVxBff_LpEBbEtwl5KnVpUEb_SZdXhJv7j7K7DyBYeZ_CiUn2Rp4voTtkHnIilkiW7KlZeUI9ZEVRWcXIOXLIulmNcB_C-pzOSZohQNO-EV0iMGclsejqtEGWR9M-3hcze0L17o17h8X?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/oy-ZmkmaPKZ2PmaZerBbjNfLgwEEQmnP6Mx2QaT_jrGfD49pl85AQjaXvceC7UgoQ9BTCQGwRJZKtez7itCVBVonknQp7jCYH7xlHEUIcGMMpoyUdhA5S7_h-4aLvty6XOXq7kAcBhsEDLKW-ggBaAS8eAifsW5gZlDjbTnNzae55I-X8ika48vH6umLqCcr?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/zEzWrzA33Zp8Bgd8mZ3XnZ9gntgAlsPv_P1ZMWE-SH6hARN8L_vONMH7PYw1zRiEQL0FpUZ52tvIsdNP5Ft1C1yYdtmB9u4PxNQhwSvmlEHLPHQd0cUlMSmFb8uu1DZ1t52nAMv5sVVMpfnkH2aeaUfEXUl4kCx9GSCGVVDBXoORLONHzW3BvINQ1l_NYCtx?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/5QdV2EhUJITQLedgWdNC6H_w0Ctiq8MeuLaZDTsTs7QMOz7Oqx-ZRX8H1G2IH72bxKR97S112hU0lYlDNv3rNMUq-yOl4-1Y8DUxhFeh-rOgtQfn8BL8cVDhneXX1LncRafNarUeKZny-nKntRfos8eC65S7ydrd9MUaBb8h3IJ6EVnpfTgv1XyTYdDRpC1M?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/dA5GXw3Plms5hjW1iZPvMAt88E7SNFSxsKSscz_NTKaV0woWBIAFoLvTf61oauJ2dGZM6BIfwIk8rm4__Gn-UVHiF5Q-IAWy4DqGyVlNpKZC0BFFTf5R3T0gAkDx124zuVzH8YNUWlBrEr_q2qqtREy2lEMFmEfy9CxYf1uiKmnUH34ywOmgyEiaON3Up2Qt?purpose=fullsize)

* Arbiter decision (halt / review / proceed)
* Confidence flow across pipeline
* Execution isolation (advisory mode)

---

### 📊 Outcome Evaluation + History

![Image](https://images.openai.com/static-rsc-4/c-UqpUrWsJj2iz_5flIbvsVt37bve4InTqwsHI3aetCo-PhDz5exY_4dWW05Cpwh3udkRxXclUS9aNKUqwV7BZwnWkxcP94TYa_hkoxsKKRGu6iqluF3MizXpo_kgGCNZAtSeJ2MRd34oLPmQFSbNZNx9iipewHeesmld2GkmLsi9SilL62nzbdA_jr47Ezv?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/kfnRDNLWVrQnApPRjzdUsdcZuAvuwFRq5OmgOcoFxY8r06sfKS5Z2qCKR2tFUDHc9ERn2STHItU5hL9TyHKFmUc_G9TMIcY0zIF808puXFEJbLL7_NK9bcUg2HbrK9ajb3vZvoYgQ_ppM2RCyew9qaeLG9c36mwfxugHxm5Bqjd2VPKIM-BcudPko5UTrZ1E?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/u-qJOsD3FvW60zcZWRMT46dnhABH8div2OYOglnARDCk6xXSQgtOwiiMJITQOvzdCXCE1-HERICmtcnOlRyn73Zklrxp2YepznvFm-mqDhhfAAilnXyrxnmpFCe7qeLxDVQxp6HWAU_Htg07GWh18i5R9uRMrTnRxhDwsmAhUyQvdF8HKYiNlYKhRBlVSoSM?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/YkCqxYSk6HR8WiUQ9bV_-gzxEaUL1wBi_F-pzupcSZfxmxmp8VmodtjYb_YUEatnWcZzdKP5ves7kT4Wxt_FioxFNcTr5r5Je0gqvxj7wQ36S8miyOzU326pce0S4ifYkr_PnCNDHVBzPQ7ONAOjycNX9uYQx0lhJLXlH7dL6jFJGmwLteTnPba8I0vnPd6e?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/6SyzOWjkx9e2I9ETGRlzlA8UDSxzHl2tYhxXD24KX5mymXG3YGYN8EqkASBdQeo7L2aDhI8qYH5nhxeaKrDd7UJzU0D4FiT0zHe5Ow7Ac7kklNbGFtubqp4QnvM-cqcs5MJiGS61v5DKhpesoER-6rQK9nvrYvl4Ilwvn3dsaqPJaokNkX94c4DbJFddYGjD?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/AODhsuYKiDchSaZXoNMN6BXOcujkyDHlhqIFEL9KNHj0OiqRJ-mxOfc1oZvrA5wBSevc7LZ6kgN55oWFS2kArkK_5b6rq97TF5rz61HAefudQU_I34Wf2whSeb7Xr77z-48R5ZtwPHm6Rq3dlCl3TbBKCy1jMOxi7m_wS0iMLPAq5tH1LI05qwNLZIvIpVQY?purpose=fullsize)

* Outcome scoring
* System health simulation
* Incident history tracking

---

## 🧱 Repository Structure

```
agents/        → reasoning units (analysis, rag, decision)
orchestrator/  → LangGraph pipeline
core/          → arbiter, metrics, config
rag/           → embeddings + retrieval
llm/           → model abstraction layer
execution/     → safe action routing
config/        → YAML-driven system behavior
ui/            → Streamlit glass-box UI
data/          → RAG knowledge base
```

---

## ⚙️ Local Setup

### Requirements

* Python 3.10+
* Podman + podman-compose
* Ollama

---

### Start infrastructure

```bash
podman compose -f infra/podman-compose.yaml up
```

---

### Python setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### Initialize RAG

```bash
python -c "from rag.setup import init_qdrant; init_qdrant()"
```

---

### Start LLM (Ollama)

```bash
brew install ollama
ollama serve
ollama pull phi
ollama run phi
```

---

### Run application

```bash
PYTHONPATH=. streamlit run ui/app.py
```

---

## ☸️ OpenShift Alignment

Designed for:

* OpenShift 4.18+
* OpenShift AI (model serving via vLLM)

Supports:

* External LLM endpoints
* Container-native deployment
* Config-driven environment switching

---

## 🔌 Extensibility

### Add new model

* Implement provider in `llm/providers/`
* Register in config

---

### Add new tool

* Update `tools.yaml`
* Implement handler in execution layer

---

### Add new signatures

* Extend `signatures.yaml`

---

## ⚠️ Known Limitations (Intentional for Demo)

* Advisory mode only (no real execution)
* Simulated outcome evaluation
* Limited RAG dataset
* No multi-tenant isolation

---

## 🚀 Future Improvements

* Observability (agent drift / arbitration metrics)
* Multi-model consensus
* Policy engine externalization (OPA)
* Event-driven pipeline (Kafka)
* Real feedback loop (RAG write-back)

---

## 🧠 Demo Value

This project demonstrates a shift from:

```text
LLM scripts → AI systems
black-box → glass-box
automation → governed decisioning
```

---

## 🏁 Final Note

This is a **high-signal architecture demo**, designed to show:

* System thinking
* Risk-aware AI design
* Enterprise-ready patterns

— not just code.
