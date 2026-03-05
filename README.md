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
```

## Milestone 2: Reflexion & Prompt Engineering

**Workflow:** `meeting_to_action.py` (updated)  
**Test Script:** `tests/test_workflows.py`

### Enhancements

- **Reflexion:** AI self-reviews its initial output to catch missing deadlines, unclear tasks, or incomplete action items
- **Chain-of-Thought (CoT):** Prompts now guide the AI through explicit reasoning steps before generating the final output
- **Two-pass validation:** Initial output is generated, then refined through a reflexion check for improved accuracy and completeness

### Input
Same as Milestone 1: a plain text meeting transcript.

### Output
Structured JSON with the same schema as Milestone 1, but now with higher reliability and completeness:

- `summary` – Key discussion points (refined for clarity)
- `action_items` – Complete list of tasks, each with owner and deadline (verified by reflexion)
- `risks` – Project risks (now more comprehensive)
- `follow_up_email` – Draft email aligned with all identified action items

**Example Output:**
```json
{
    "summary": "The team discussed that Project X is experiencing a delay due to resource constraints. Alice committed to preparing a detailed report on the issue, and Bob agreed to inform all stakeholders about the schedule change.",
    "action_items": [
        {
            "owner": "Alice",
            "task": "Prepare the resource-issue report for Project X",
            "deadline": "2026-03-11"
        },
        {
            "owner": "Bob",
            "task": "Notify stakeholders about the project delay and share Alice's report",
            "deadline": "2026-03-11"
        }
    ],
    "risks": [
        "Continued resource shortages may further extend the project timeline.",
        "Stakeholder dissatisfaction due to lack of timely communication.",
        "Potential impact on downstream deliverables that depend on Project X."
    ],
    "follow_up_email": "Subject: Update on Project X..."
}
```
