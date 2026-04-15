
import os
from openai import OpenAI
from rag.vector_store import retrieve_context

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm(prompt):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content

def analysis_agent(log):
    return llm(f"Summarize this log issue: {log}")

def diagnosis_agent(log):
    context = retrieve_context(log)
    return llm(f"Given log: {log} and context: {context}, find root cause")

def fix_agent(diagnosis):
    return llm(f"Suggest a safe fix for: {diagnosis}")
