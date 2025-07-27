"""Link glyph symbols from the codex to known entities in the registry."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def load_entity_registry(file_path: Path | str) -> List[Dict[str, Any]]:
    """Load a JSON registry file describing entities."""
    path = Path(file_path)
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        return list(data.get("entities", []))
    return data


def map_glyphs_to_entities(
    glyph_data: Dict[str, Dict[str, Any]],
    entity_registry: List[Dict[str, Any]],
) -> Dict[str, List[Dict[str, Any]]]:
    """Connect each glyph to matching or suggested entities from registry.

    Matching is case-insensitive and supports partial name overlaps.
    """

    mapping: Dict[str, List[Dict[str, Any]]] = {}
    for glyph, info in glyph_data.items():
        mapping[glyph] = []
        glyph_entities = [e.lower() for e in info.get("entities", [])]
        for entity in entity_registry:
            name = entity.get("name", "").lower()
            if not name:
                continue
            if name in glyph_entities:
                mapping[glyph].append(entity)
                continue
            for ge in glyph_entities:
                if ge in name or name in ge:
                    mapping[glyph].append(entity)
                    break
    return mapping
