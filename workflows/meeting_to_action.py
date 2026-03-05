from utils.ai_client import call_ai

def meeting_to_action(transcript):
    prompt = f"""
You are a smart assistant. Your task is to read the meeting transcript and extract:

1. Summary of key discussion points.
2. Action items with owner and deadline.
3. Risks mentioned.
4. Draft follow-up email.

Instructions:
- Reason step by step (Chain-of-Thought).
- After generating the first output, review it and fix any missing items (Reflexion).
- Return ONLY a valid JSON object with keys: summary, action_items, risks, follow_up_email.

Meeting transcript:
\"\"\"{transcript}\"\"\"
"""
    output = call_ai(prompt)
    return output