import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), 'agent.log')

def log_action(action: str) -> None:
    """Append a timestamped action to the log file in plain text."""
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} - {action}\n")

if __name__ == '__main__':
    # Example usage
    log_action('Example action logged')
