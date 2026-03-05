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

print(output)