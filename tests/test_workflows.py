import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from workflows.meeting_to_action import meeting_to_action

# Example meeting transcript
transcript = """
Project X is delayed due to resource issues. 
Alice will prepare the report by Friday. 
Bob will notify stakeholders about the change.
"""

# Run workflow
output = meeting_to_action(transcript)

# Try parsing as JSON
try:
    parsed = json.loads(output)
    print(json.dumps(parsed, indent=4))
except json.JSONDecodeError:
    print("AI output was not valid JSON:")
    print(output)