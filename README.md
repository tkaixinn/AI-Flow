# AI-Flow

AI-Flow is a Python-based AI workflow automation platform. It processes meeting transcripts and other business documents to automatically generate actionable insights.

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-green)](https://ai-flow.streamlit.app)

## Live Demo

Try AI-Flow here: [AI-Flow Live Demo](https://ai-flow.streamlit.app)

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
- Same as Milestone 1: a plain text meeting transcript.
- Can be extended to other document types or workflows by creating a new YAML file and corresponding Python function

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
Same as Milestone 1: a plain text meeting transcript.

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

## Milestone 6: Streamlit Dashboard 

## Overview 
Milestone 6 focuses on building a **user-friendly platform using Streamlit** for AI-Flow workflows. The goal is to make AI-driven workflow outputs accessible to both business and technical users without requiring coding knowledge.

## Features
### 1. Workflow Selection
- Users can choose between available workflows:
  - **Meeting Workflow**: Converts meeting transcripts into structured action items.
  - **Risk Assessment Workflow**: Analyzes project plans to identify potential risks.

### 2. Input Options
- **Paste text** directly into the sidebar.  
- **Upload a `.txt` file** containing input.  

### 3. Tabbed Interface
- **🚀 Run Workflow**: Execute workflows and view outputs.  
- **📘 Workflow Guide**: Provides clear instructions on what to include in each workflow input, with examples and expected outputs.

### 4. Readable Output
- Workflow results are displayed in a **business-friendly, structured format** using paragraphs, headings, and bullet points.  
- Designed to be **easy to read** for non-technical users.

### 5. JSON Output (Technical Users)
- Users can download the raw workflow output as a JSON file for **technical use**.  
- The JSON is **indented for readability** and preserves structured data.

## Steps to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open the URL displayed in your terminal (usually `http://localhost:8501`).

4. Select a workflow, provide input, and click **Run Workflow**.

5. View output in **Readable Output** or download as JSON.

## Notes
- **Readable Output**: Formatted for business users and uses HTML for styling in the dashboard.  
- **JSON Output**: Designed for technical users; suitable for programmatic consumption or further processing.  
- **Workflow Guide**: Ensures users know what to provide as input, making the platform intuitive.

## Milestone 7: Streamlit Deployment

### Overview
Deploy AI-Flow as a web application for easy access without requiring local Python setup.

### Deployment Details
- Deployed on **Streamlit Cloud**, tagged as **v1.0** for the first stable release.

**Deployment Summary:**
- Project hosted on GitHub and linked to Streamlit Cloud.
- `app.py` used as the entry point with all dependencies specified in `requirements.txt`.
- Deployment verified to ensure smooth functionality and accessibility.

## Milestone 8: Refined Readable Outputs & Streamlit Presentation

### Overview
This milestone enhances the presentation of workflow outputs for **non-technical users**, making AI-Flow results immediately actionable and visually clear. Outputs are now formatted with indentations and sections, improving readability and professional appearance. 

### Enhancements
- **Error Handling:** Recursive extraction of meaningful AI outputs, unwrapping any error-wrapped responses.  
- **Readable Output Formatting:** Nested JSON outputs are displayed in a business-friendly format using headings, bullets, and spacing.  

### Input
Same as previous milestones: plain text meeting transcripts or project plans.

### Output
Readable, structured, business-friendly output alongside JSON. 

### Impact 
Improves end-user experience, reduces cognitive load, and ensures stakeholders can quickly interpret and act on AI-generated insights.