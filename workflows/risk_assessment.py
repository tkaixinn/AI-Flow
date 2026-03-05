import json
from utils.ai_client import call_ai

def risk_assessment(project_text):
    prompt = f"""
You are a smart assistant. Your task is to read the project plan or proposal and extract potential risks:

Step 1: Read the project document carefully.
Step 2: Identify each potential risk.
Step 3: For each risk, provide:
       - risk_description
       - likelihood (High, Medium, Low)
       - impact (High, Medium, Low)
       - mitigation_plan
Step 4: Return all outputs in JSON format with key: risks.

Instructions:
- Reason step by step (Chain-of-Thought).
- After generating the first output, review it and fix any missing items (Reflexion).
- Return ONLY a valid JSON object with key: risks.

**CRITICAL INSTRUCTION:**
Return ONLY the corrected JSON. 
NO explanations. NO tables. NO comments. NO markdown.
Just the raw JSON object starting with {{ and ending with }}.

Example of correct response format:
{{"risk_description": "...", "likelihood": "...", "impact": "...", "mitigation_plan": "..."}}


Project text:
\"\"\"{project_text}\"\"\"
"""
    initial_output = call_ai(prompt)

    refined_output = reflexion_check(initial_output)

    try:
        return json.loads(refined_output)
    except json.JSONDecodeError:
        return {"error": refined_output}


def reflexion_check(output_json):
    prompt = f"""
Review this workflow output and check for errors:
1. Are all risks complete with description, likelihood, impact, and mitigation_plan?
2. Are the likelihoods and impacts reasonable based on the project context?
3. Are any risks missing or duplicated?

Correct any mistakes and return JSON in the same format.

Your ENTIRE response must be a single, valid JSON object starting with {{ and ending with }}.

**EXAMPLE OF FORBIDDEN RESPONSE (DON'T DO THIS):**
**Review Findings** | # | Issue | ... | **Corrected JSON** ```json {{...}}```

**EXAMPLE OF CORRECT RESPONSE (DO THIS EXACTLY):**
{{"risks": [...]}}

Output to check:
{output_json}
"""
    return call_ai(prompt)