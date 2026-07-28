"""
Airia Pipeline Feed Script

How to use:
1. Set your API key
2. Update PIPELINE_ID with the pipeline you want to inspect
3. Run the script — it fetches the most recent execution and prints each step's output
"""

import requests

# UPDATE THESE VALUES
API_KEY = "ak-YOUR_API_KEY_HERE"
PIPELINE_ID = "your-pipeline-id"

HEADERS = {"X-API-Key": API_KEY}


def get_execution_ids():
    response = requests.get(
        "https://prodaus.api.airia.ai/v1/Feed/pipelines",
        params={"pageNumber": 1, "pageSize": 50, "sortBy": "createdAt", "sortDirection": "DESC", "pipelineId": PIPELINE_ID},
        headers=HEADERS
    )
    return response.json()["items"]


def get_feed(execution_id):
    response = requests.get(
        f"https://prodaus.api.airia.ai/v1/Feed/pipelines/{execution_id}",
        headers=HEADERS
    )
    return response.json()


# EXECUTION
first_id = get_execution_ids()[0]["id"]
data = get_feed(first_id)

print(f"Execution: {data['ExecutionId']}")
print(f"Success:   {data['Success']}")
print()

for step in data["StepsExecutionContext"].values():
    result = step.get("Result") or {}
    value = result.get("Value", "")
    print(f"[{step['StepTitle']}]")
    print(value[:500] if value else "(no output)")
    print()
