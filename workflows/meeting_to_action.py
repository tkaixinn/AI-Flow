from utils.ai_client import call_ai

def meeting_to_action(transcript):
    prompt = f"""
You are a smart assistant. Your task is to read the meeting transcript and extract:

Step 1: Read the transcript carefully.
Step 2: Summarize key discussion points.
Step 3: List all action items with owner and deadline.
Step 4: Identify potential risks.
Step 5: Draft a follow-up email for stakeholders.
Return all outputs in JSON format with keys: summary, action_items, risks, follow_up_email.

Instructions:
- Reason step by step (Chain-of-Thought).
- After generating the first output, review it and fix any missing items (Reflexion).
- Return ONLY a valid JSON object with keys: summary, action_items, risks, follow_up_email.

    
**CRITICAL INSTRUCTION:**
Return ONLY the corrected JSON. 
NO explanations. NO tables. NO comments. NO markdown.
Just the raw JSON object starting with {{ and ending with }}.

Example of correct format:
{{"summary": "...", "action_items": [...], "risks": [...], "follow_up_email": "..."}}

Meeting transcript:
\"\"\"{transcript}\"\"\"
"""
    initial_output = call_ai(prompt)

    refined_output = reflexion_check(initial_output)

    return refined_output

def reflexion_check(output_json):
    prompt = f"""
    Review this workflow output and check for errors:
    1. Are all action items complete with owner and deadline?
    2. Are risks clearly stated and relevant?
    3. Is the follow-up email accurate based on action items?

    Correct any mistakes and return JSON in the same format.

    Output to check:
    {output_json}
    """
    return call_ai(prompt)
