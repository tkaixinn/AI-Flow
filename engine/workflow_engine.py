import yaml
from workflows.meeting_to_action import meeting_to_action
from workflows.risk_assessment import risk_assessment

FUNCTION_MAP = {
    "meeting_to_action": meeting_to_action,
    "risk_assessment": risk_assessment

}


def run_workflow(workflow_path, input_data):
   
    if not workflow_path.endswith('.yaml'):
        workflow_path = f"workflow_configs/{workflow_path}.yaml"
    
    with open(workflow_path, "r") as f:
        config = yaml.safe_load(f)

    outputs = {}

    for step in config["steps"]:
        func_name = step["function"]

        if func_name not in FUNCTION_MAP:
            raise ValueError(f"Function {func_name} not registered")

        func = FUNCTION_MAP[func_name]

        result = func(input_data)

        outputs[step["name"]] = result

    return outputs