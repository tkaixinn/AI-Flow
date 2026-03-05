import sys
import json
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine.workflow_engine import run_workflow

project_text = """
Project Alpha aims to launch a new product by Q3.
Potential resource constraints may delay development.
Testing team may not complete QA on time.
Marketing dependencies may cause launch misalignment.
"""

output = run_workflow(
    "workflow_configs/risk_assessment_workflow.yaml",
    project_text
)

parsed_output = {}
for key, value in output.items():
   if isinstance(value, str):
       try:
           parsed_output[key] = json.loads(value)
       except json.JSONDecodeError:
           parsed_output[key] = value
   else:
       parsed_output[key] = value


print(json.dumps(parsed_output, indent=2))
