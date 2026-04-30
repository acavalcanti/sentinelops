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

## ADR-005 — Analysis Confidence Model

**Context**

The analysis agent invokes an LLM to reason about an incident log. A confidence
score is required downstream by the arbiter to make a governance decision.
The natural approach would be to ask the LLM to self-report its own confidence.

***Decision***

Use a bounded random signal (`base + uniform(variance_min, variance_max)`)
rather than LLM self-reported confidence.

***Rationale***

- **LLM self-reported confidence is unreliable.** Small models (phi, mistral)
  consistently over-report confidence regardless of actual output quality.
  Self-assessment scores cluster near 0.9 and provide no discriminating signal.
- **Hedging-language heuristics are model-dependent.** Parsing phrases like
  "I think" or "possibly" requires prompt tuning per model family, which
  conflicts with the multi-provider abstraction goal.
- **Bounded variance honestly represents epistemic uncertainty.** In a real
  system, analysis confidence would derive from ensemble agreement or
  calibration data neither of which exists in a demo context. Random variance
  within a realistic range (`0.6–0.9`) is more honest than a fake precise
  number extracted from LLM output.

***Tradeoffs***

| Option                  | Pro                   | Con                                  |
|-------------------------|-----------------------|--------------------------------------|
| LLM self-report         | Feels "real"          | Unreliable, model-specific, inflated |
| Hedging heuristic       | Cheap proxy           | Fragile, prompt-dependent            |
| Bounded random (chosen) | Honest, config-driven | Not a real measurement               |

***Consequences***

- Confidence parameters (`base`, `variance_min`, `variance_max`) are
  externalized to `config.yaml` so the range can be tuned per demo context.
- The UI surfaces a note acknowledging the simulated variance.
- A production system would replace this with calibration data or an
  ensemble signal. This is explicitly listed as a future improvement.

---

## Summary

These decisions prioritize:

* Explainability
* Safety
* Architectural clarity

over:

* Full automation
* Production completeness
