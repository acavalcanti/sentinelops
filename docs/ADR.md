# Architecture Decision Records — SentinelOps AI

## ADR-001 — Confidence Arbiter (Weighted vs Rule-Based)

**Context**
The system must decide whether to execute, halt, or review an AI-generated action. This decision must balance multiple signals (LLM reasoning, RAG relevance, deterministic patterns).

**Decision**
We use a **weighted confidence model** instead of a rule-based system.

**Rationale**

* Allows combining heterogeneous signals (probabilistic + deterministic)
* More flexible than rigid rule chains
* Easier to tune via configuration (YAML-driven weights)
* Reflects real-world uncertainty rather than binary logic

**Tradeoffs**

* Less deterministic than rule engines
* Requires calibration of weights

---

## ADR-002 — Advisory Mode as First-Class Concept

**Context**
Executing AI-generated actions directly introduces operational risk.

**Decision**
Execution is implemented as **advisory-only**, not as a feature toggle.

**Rationale**

* Enforces safety by design (not optional)
* Aligns with real enterprise adoption patterns (AI copilots)
* Allows system to focus on reasoning + governance

**Tradeoffs**

* No real automation in demo
* Requires explanation in documentation

---

## ADR-003 — YAML Policy Instead of OPA/Rego

**Context**
We need a policy layer to validate actions.

**Decision**
Use **YAML-based policy definitions** instead of OPA/Rego.

**Rationale**

* Simpler for demo and readability
* No external dependency required
* Easier for reviewers to understand quickly

**Tradeoffs**

* Less expressive than full policy engines
* Not production-grade enforcement

---

## ADR-004 — RAG as Policy/Knowledge Layer

**Context**
The system needs contextual knowledge for decision-making.

**Decision**
Use **RAG (Qdrant)** instead of static mappings.

**Rationale**

* Enables extensibility without code changes
* Aligns with modern AI system patterns
* Demonstrates knowledge grounding

**Tradeoffs**

* Requires vector DB setup
* Small dataset limits demo realism

---

## Summary

These decisions prioritize:

* Explainability
* Safety
* Architectural clarity

over:

* Full automation
* Production completeness
