# Chatgbt

This repository includes utilities for logging agent actions.

## Logging actions

Use `agent_logger.log_action` to append a timestamped message to `agent.log`.
A simple example:

```python
from agent_logger import log_action

log_action('Agent started task')
```

## Fetching SkyCrypt data

`skycrypt_fetcher.py` demonstrates how to request profile data and log each
step. Running the module will attempt to contact `sky.shiiyu.moe`, which may
fail due to the site's Cloudflare protection. Logged messages record the
result of the request.
