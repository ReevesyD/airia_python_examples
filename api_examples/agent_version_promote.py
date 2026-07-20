import requests

API_KEY  = "YOUR_API_KEY"
AGENT_ID = "YOUR_AGENT_ID"

HEADERS = {"X-API-Key": API_KEY, "Content-Type": "application/json"}
BASE    = "https://prodaus.api.airia.ai"


def list_versions():
    r = requests.get(f"{BASE}/v1/PipelinesConfig/{AGENT_ID}", headers=HEADERS)
    config = r.json()
    for v in config["versions"]:
        active = "<-- ACTIVE" if v.get("id") == config.get("activeVersionId") else ""
        print(v.get("versionNumber"), v.get("id"), active)
    return config


def promote_version(config, target_version_id):
    response = requests.put(f"{BASE}/v1/PipelinesConfig/{AGENT_ID}", headers=HEADERS, json={
        "id": AGENT_ID,
        "activeVersionId": target_version_id,
        "projectId": config["projectId"]
    })
    print("Status:", response.status_code)
    print("Body:", response.text[:300])


config = list_versions()
# promote_version(config, "PASTE_UUID_HERE")