"""Utilities for parsing glyph CSV files into dictionaries."""

import csv
from pathlib import Path
from typing import Dict, List

def parse_glyph_csv(file_path: Path | str) -> Dict[str, Dict[str, List[str]]]:
    """Parse a glyph encyclopedia CSV into a dictionary keyed by glyph."""
    csv_path = Path(file_path)
    glyphs: Dict[str, Dict[str, List[str]]] = {}
    with csv_path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            glyph = (row.get("Glyph") or row.get("glyph") or row.get("symbol") or "").strip()
            if not glyph:
                continue
            entities = row.get("Entity") or row.get("entities") or ""
            entities_list = [e.strip() for e in entities.split(";") if e.strip()]
            glyphs[glyph] = {
                "literal": row.get("Literal Meaning", row.get("literal", "")).strip(),
                "affective": row.get("Affective Meaning", row.get("affective", "")).strip(),
                "entities": entities_list,
            }
    return glyphs


if __name__ == "__main__":
    import pprint
    import sys

    csv_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/glyph_codex.csv")
    pprint.pprint(parse_glyph_csv(csv_file))
