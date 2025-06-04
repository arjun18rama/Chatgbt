"""Simple logging utilities for agent actions."""

from __future__ import annotations

import logging
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "agent.log")

_logger = logging.getLogger(__name__)
_handler_initialized = False


def _init_logger() -> None:
    """Initialize the underlying :mod:`logging` handler if needed."""
    global _handler_initialized
    if _handler_initialized:
        return
    _logger.setLevel(logging.INFO)
    handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
    _logger.addHandler(handler)
    _handler_initialized = True


def log_action(action: str) -> None:
    """Append a timestamped action to the log file."""
    _init_logger()
    _logger.info(action)


def read_log(lines: int = 10) -> list[str]:
    """Return the last ``lines`` entries from the log file."""
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.readlines()[-lines:]

if __name__ == '__main__':
    # Example usage
    log_action('Example action logged')
