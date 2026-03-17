
"""
Airia OnDemand Processing Upload Script

How to use:
1. Set your API key
2. Update FILE_PATH with the file you want to process
3. Run the script
"""

import os
import requests

# UPDATE THESE VALUES
API_KEY = "ak-YOUR_API_KEY_HERE"
FILE_PATH = "YOUR_FILE_PATH_HERE"

MIME_TYPES = {
    ".pdf":  "application/pdf",
    ".doc":  "application/msword",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".txt":  "text/plain",
    ".xls":  "application/vnd.ms-excel",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
}

def process_file_on_demand(filepath):
    """Upload a file to Airia OnDemand Processing and return the signed URL"""
    file_name = os.path.basename(filepath)
    file_ext = os.path.splitext(filepath)[1].lower()
    mime_type = MIME_TYPES.get(file_ext)

    with open(filepath, "rb") as f:
        response = requests.post(
            "https://prodaus.api.airia.ai/v1/upload/onDemandProcessing",
            headers={"X-API-Key": API_KEY},
            files={"file": (file_name, f, mime_type)}
        )

    return response.json().get("signedURL")


# EXECUTION
signed_url = process_file_on_demand(FILE_PATH)

print(f"Signed URL: {signed_url}")