"""Functions for generating canonical codex entries from glyph usage data."""

from typing import Any, Dict


def generate_codex_entry(glyph: str, usage_data: Dict[str, Any]) -> str:
    """Composes canonical-style Codex entry for a glyph."""
    lines = [f"# Glyph: {glyph}\n"]
    literal = usage_data.get('literal')
    affective = usage_data.get('affective')
    entities = usage_data.get('entities', [])
    if literal:
        lines.append(f"Literal Meaning: {literal}")
    if affective:
        lines.append(f"Affective Meaning: {affective}")
    if entities:
        lines.append("Entities: " + ", ".join(entities))
    return "\n".join(lines)
