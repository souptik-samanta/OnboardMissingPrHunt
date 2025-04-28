import requests
import sys

YSWS_API_URL = "https://verify.hackclub.dev/api/status"

def check_ysws_status(slack_id):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "slack_id": slack_id
    }

    try:
        response = requests.post(YSWS_API_URL, json=data, headers=headers)
        response.raise_for_status()
        text = response.text.strip()

        if "Eligible L1" in text:
            return "✅ Eligible Level 1"
        elif "Eligible L2" in text:
            return "✅ Eligible Level 2"
        elif "Ineligible" in text:
            return "❌ Ineligible"
        elif "Insufficient" in text:
            return "⚠️ Insufficient Activity"
        elif "Sanctioned Country" in text:
            return "🚫 Sanctioned Country"
        elif "Testing" in text:
            return "🧪 Testing Status"
        else:
            return "❓ Unknown Response"

    except requests.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ysws_check.py <slack_id>")
        sys.exit(1)

    slack_id = sys.argv[1]
    status = check_ysws_status(slack_id)
    print(f"Slack ID: {slack_id} → {status}")
