# src/tools/logger.py
import csv, os, datetime as dt
LOG_PATH = "data/usage_log.csv"

def log_run(query: str, outcomes: dict, resources: list, score: float):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    new = not os.path.exists(LOG_PATH)
    with open(LOG_PATH, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["timestamp","query","content_outcomes","ws_outcomes","picks","score"])
        picks = "; ".join([r.get("id","") for r in resources])
        w.writerow([
            dt.datetime.now().isoformat(timespec="seconds"),
            query,
            "|".join(outcomes.get("content_outcomes", [])),
            "|".join(outcomes.get("ws_outcomes", [])),
            picks,
            score,
        ])
