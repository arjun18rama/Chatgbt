import csv
import random
import time
from datetime import datetime
from typing import Optional

import requests

from agent_logger import log_action

API_URL_TEMPLATE = "https://api.mcsrvstat.us/2/{server}"
CSV_FILE = "player_count.csv"

def fetch_player_count(server: str) -> Optional[int]:
    """Return the number of players currently online for the server."""
    url = API_URL_TEMPLATE.format(server=server)
    log_action(f"Requesting {url}")
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        log_action(f"Received status {response.status_code} from {url}")
        response.raise_for_status()
        data = response.json()
        return data.get("players", {}).get("online")
    except requests.RequestException as exc:
        log_action(f"Failed to fetch player count: {exc}")
        return None

def append_to_csv(timestamp: str, count: Optional[int]) -> None:
    """Append a timestamp and player count to the CSV file."""
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, count if count is not None else ""])


def poll_player_count(server: str) -> None:
    """Continuously poll player count roughly every minute with jitter."""
    while True:
        timestamp = datetime.utcnow().isoformat()
        count = fetch_player_count(server)
        append_to_csv(timestamp, count)
        # sleep for about one minute with random jitter
        delay = 60 + random.uniform(-10, 10)
        log_action(f"Sleeping for {delay:.2f} seconds")
        time.sleep(delay)


if __name__ == "__main__":
    poll_player_count("play.hypixel.net")
