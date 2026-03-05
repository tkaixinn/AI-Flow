import sys
import json
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine.workflow_engine import run_workflow

transcript = """
Project X is delayed due to resource issues.
Alice will prepare the report by Friday.
Bob will notify stakeholders about the change.
"""

output = run_workflow(
   "workflow_configs/meeting_workflow.yaml",
   transcript
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
