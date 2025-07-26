"""Simple query utilities for the Sanctuary Codex engine."""

from typing import Any, Dict, Iterable, List


def entities_for_glyph(glyph: str, glyph_data: Dict[str, Dict[str, Any]]) -> List[str]:
    """Return entity names associated with a glyph from the codex."""
    info = glyph_data.get(glyph, {})
    return info.get("entities", [])


def glyphs_for_entity(entity: str, glyph_data: Dict[str, Dict[str, Any]]) -> List[str]:
    """Return glyphs that reference the given entity name (case-insensitive)."""
    results = []
    lowered = entity.lower()
    for glyph, info in glyph_data.items():
        entities = [e.lower() for e in info.get("entities", [])]
        if any(lowered == e or lowered in e for e in entities):
            results.append(glyph)
    return results


def search_literal(term: str, glyph_data: Dict[str, Dict[str, Any]]) -> List[str]:
    """Find glyphs whose literal meaning contains the term (case-insensitive)."""
    results = []
    lowered = term.lower()
    for glyph, info in glyph_data.items():
        literal = info.get("literal", "").lower()
        if lowered in literal:
            results.append(glyph)
    return results


if __name__ == "__main__":
    import pprint
    from pathlib import Path
    from glyph_parser import parse_glyph_csv

    codex = parse_glyph_csv(Path("data/glyph_codex.csv"))
    pprint.pprint(entities_for_glyph("🜏", codex))
    pprint.pprint(glyphs_for_entity("Finalis", codex))
    pprint.pprint(search_literal("Pain", codex))

