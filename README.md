# AI-Flow

AI-Flow is a Python-based AI workflow automation platform. It processes meeting transcripts and other business documents to automatically generate actionable insights.

## Milestone 1: Meeting Workflow

**Workflow:** `meeting_to_action.py`  
**Test Script:** `tests/test_workflows.py`

### Overview
This workflow processes meeting transcripts and automatically extracts key outcomes from discussions. The AI analyzes the transcript, summarizes the discussion, identifies action items with responsible owners and deadlines, detects potential risks, and drafts a follow-up email to stakeholders.

### Input
A meeting transcript in plain text.  

**Example Input:**
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

## Milestone 3: YAML Workflow Engine

**Engine:** `engine/workflow_engine.py`  
**Workflow Configs:** `workflow_configs/meeting_workflow.yaml`  
**Test Script:** `tests/test_workflows.py`

### Overview
Milestone 3 introduces a **generic workflow engine** that reads YAML configuration files to run AI workflows. This allows multiple business workflows to be added without modifying Python code.  

The engine executes workflows in the following sequence:

1. Load the YAML workflow definition
2. Map each step's function name to its corresponding Python function
3. Execute the Python function with the input data
4. Collect structured JSON outputs

This design separates **workflow logic** from **workflow configuration**, enabling scalable, citizen-developer-ready AI automation.

### Input
- Plain text meeting transcript (same as Milestone 1 & 2)
- Can be extended to other document types or workflows by creating a new YAML file and corresponding Python function

**Example Input:**
Same as Milestone 1: a plain text meeting transcript.

### YAML Workflow Definition
Example `workflow_configs/meeting_workflow.yaml`:

```yaml
workflow_name: meeting_workflow
steps:
  - name: meeting_to_action
    function: meeting_to_action
    description: "Convert meeting transcript into structured JSON with summary, action_items, risks, follow_up_email."

```
### Output 
Structured JSON, same schema as Milestone 2

## Milestone 4: Risk Assessment Workflow

**Workflow:** `risk_assessment.py`  
**Workflow Config:** `workflow_configs risk_assessment_workflow.yaml`
**Test Script:** `tests/test_risk_assessment.py`

### Overview
Milestone 4 allows project managers to identify and mitigate potential risks in project plans or proposals. The AI analyzes the input text, categorizes risks, evaluates likelihood and impact, and suggests mitigation plans.

It uses **Chain-of-Thought (CoT)** reasoning and **Reflexion** to ensure completeness and accuracy.

### Input
Project plans or proposals as plain text.

**Example Input:**
Project Alpha aims to launch a new product by Q3.
Potential resource constraints may delay development.
Testing team may not complete QA on time.
Marketing dependencies may cause launch misalignment.

### YAML Workflow Definition
Example `workflow_configs/meeting_workflow.yaml`:

```yaml
workflow_name: meeting_workflow
steps:
  - name: meeting_to_action
    function: meeting_to_action
    description: "Convert meeting transcript into structured JSON with summary, action_items, risks, follow_up_email."

```
### Output
Structured JSON containing:

- `risk_description` – Description of the identified project risk
- `likelihood` – Estimated probability of the risk occurring (High, Medium, Low)
- `impact` – Severity of the risk if it occurs (High, Medium, Low)
- `mitigation_plan` – Recommended actions to reduce or manage the risk

**Example Output:**
```json
{
  "risks": [
    {
      "risk_description": "Project delay due to limited developer resources",
      "likelihood": "High",
      "impact": "High",
      "mitigation_plan": "Allocate additional developers or adjust project timeline to accommodate resource constraints."
    }
  ]
}
```
## Milestone 5: CLI Workflow Runner

**CLI Script:** `run_workflow.py`  
**Tested Workflows:** `meeting_to_action.py`, `risk_assessment.py`  

### Overview
Milestone 5 introduces a **command-line interface (CLI)** that allows users to run any workflow defined in YAML using a simple text file as input. The CLI executes the workflow using the workflow engine and outputs structured JSON directly in the terminal.  

This milestone demonstrates modularity and prepares the system for future non-technical interfaces, like a web app.

### Features
- Run multiple workflows from the terminal (e.g., `meeting_workflow`, `risk_assessment_workflow`)  
- Accepts an input text file  
- Executes the selected workflow via `workflow_engine.run_workflow()`  
- Prints structured JSON output in a readable format  

### CLI Usage
```bash
python run_workflow.py <workflow_name> <input_file>
```
**Example:**
python run_workflow.py meeting_workflow inputs/meeting1.txt

### Input
A plain text file containing the input for the workflow.

**Example Input File (**```inputs/meetings.txt```**):**
Project X is delayed due to resource issues.
Alice will prepare the report by Friday.
Bob will notify stakeholders about the change.

### Output 
Structured JSON, same schema as Milestone 2

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

