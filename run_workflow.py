import sys
import json
from engine.workflow_engine import run_workflow


def main():
    if len(sys.argv) != 3:
        print("Usage: python run_workflow.py <workflow_name> <input_file>")
        return

    workflow_name = sys.argv[1]
    input_file = sys.argv[2]

    with open(input_file, "r") as f:
        input_text = f.read()

    result = run_workflow(workflow_name, input_text)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()