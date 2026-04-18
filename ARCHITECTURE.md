# SentinelOps AI — Architecture

## Problem

LLMs are probabilistic and can produce incorrect or unsafe actions when used directly in operational environments.

## Goal

Demonstrate a governed AI system where:
- LLM reasoning is controlled
- Decisions are validated
- Actions are never executed blindly

## Architecture Overview

Log
→ Analysis (LLM)
→ Signature Matching
→ RAG Retrieval
→ Decision
→ Policy (Deterministic)
→ Arbiter (Confidence Gate)
→ Execution (Advisory)
→ Metrics / Feedback

## Key Design Principles

### 1. Separation of Concerns

- Reasoning → LLM
- Validation → Policy
- Control → Arbiter

### 2. Probabilistic vs Deterministic

LLM = probabilistic  
Policy = deterministic  

### 3. Governance Layer

The system does not trust the LLM output directly.

### 4. Explainability (Glass Box)

Every step is exposed in the UI:
- Analysis
- RAG context
- Decision
- Confidence
- Arbiter verdict

### 5. Advisory Mode

Execution is simulated to ensure safety.

## Why These Choices?

### LangGraph
Explicit state machine → traceable execution

### Qdrant (RAG)
Retrieval grounded in operational knowledge

### YAML Config
Policy-as-code → flexible and auditable

### MCP Layer (future-ready)
Decouples execution from reasoning

## Future Improvements

- Multi-tenancy
- Observability (agent drift)
- Token cost optimization