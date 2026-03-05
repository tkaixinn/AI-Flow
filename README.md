# AI-Flow

AI-Flow is a Python-based AI workflow automation platform. It processes meeting transcripts and other business documents to automatically generate actionable insights.

## Milestone 1: Meeting Workflow

**Workflow:** `meeting_to_action.py`  
**Test Script:** `tests/test_workflows.py`

### Input
A meeting transcript in plain text.  
Example:
Project X is delayed due to resource issues.
Alice will prepare the report by Friday.
Bob will notify stakeholders about the change.

### Output
Structured JSON containing:

- `summary` – A short summary of the discussion
- `action_items` – List of tasks with owners and deadlines
- `risks` – Identified project risks
- `follow_up_email` – Draft email to stakeholders

**Example Output:**
```json
{
  "summary": "Project X is delayed due to resource constraints...",
  "action_items": [
    {"owner": "Alice", "task": "Prepare report", "deadline": "2026-03-11"},
    {"owner": "Bob", "task": "Notify stakeholders", "deadline": "2026-03-11"}
  ],
  "risks": ["Resource constraints causing delay"],
  "follow_up_email": "Subject: Update on Project X..."
}

