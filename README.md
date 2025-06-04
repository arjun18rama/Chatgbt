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

## Polling player count

`player_count_poller.py` polls the online player count for a Minecraft server
using the [mcsrvstat.us](https://mcsrvstat.us/) API. Results are appended to
`player_count.csv` with a timestamp. The script waits roughly one minute
between requests with a small amount of random jitter.

Run the module directly to begin polling:

```bash
python player_count_poller.py
```
