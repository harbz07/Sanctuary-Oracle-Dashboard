"""Ingest and index ritual log files for the Sanctuary Codex engine."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List


def load_logs(paths: Iterable[Path | str]) -> List[str]:
    """Return a list of log lines from the given file paths."""
    lines: List[str] = []
    for p in paths:
        path = Path(p)
        if not path.exists():
            continue
        if path.suffix.lower() == ".json":
            with path.open(encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    lines.extend(str(entry) for entry in data)
                else:
                    lines.append(str(data))
        else:
            with path.open(encoding="utf-8") as f:
                lines.extend(l.strip() for l in f if l.strip())
    return lines


def index_logs(lines: Iterable[str]) -> Dict[int, str]:
    """Return a simple index of logs keyed by line number."""
    return {i: line for i, line in enumerate(lines)}


if __name__ == "__main__":
    import pprint
    sample_logs = load_logs(["data/sample_log.txt"])
    pprint.pprint(index_logs(sample_logs))

