import json
from typing import Any, Dict
import requests

from agent_logger import log_action

BASE_URL = "https://sky.shiiyu.moe/api/v2/profile"


def get_profile_data(username: str) -> Dict[str, Any]:
    """Fetch SkyCrypt profile data for the given username.

    This function logs the request and any errors. Note that the
    request may fail due to Cloudflare protection on the site.
    """
    url = f"{BASE_URL}/{username}"
    log_action(f"Requesting {url}")
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        log_action(f"Received status {response.status_code} from {url}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        log_action(f"Failed to fetch profile data: {exc}")
        return {}


def send_to_cbt40(payload: Dict[str, Any]) -> None:
    """Placeholder for sending data to another service.

    The payload is logged in plain text.
    """
    log_action(f"Sending payload: {json.dumps(payload)}")


if __name__ == "__main__":
    username = "BaconPanckes"
    data = get_profile_data(username)
    if not data:
        log_action("No data retrieved; aborting example")
    else:
        profile_id = next(iter(data.get("data", {}).get("profiles", {})))
        profile = data["data"]["profiles"][profile_id]
        payload = {
            "username": username,
            "profile_name": profile.get("cute_name"),
            "coins": profile.get("banking", {}).get("balance", 0),
            "purse": profile.get("networth", {}).get("data", {}).get("purse", 0),
            "armor": profile.get("inventory", {}).get("armor", []),
        }
        send_to_cbt40(payload)

