from rule_engine import extract_errors
from ollama_client import ask_ollama


def analyze_logs(logs: str, question: str):
errors = extract_errors(logs)
error_text = "\n".join(errors[:50]) # limit context


prompt = f"""
You are a senior site reliability engineer.
Given the following application logs:
{error_text}


Answer this question:
{question}


Return structured insights including:
- Root cause
- Error frequency
- Recommendation
"""

ai_response = ask_ollama(prompt)

return {
    "error_count": len(errors),
    "ai_analysis": ai_response
}
