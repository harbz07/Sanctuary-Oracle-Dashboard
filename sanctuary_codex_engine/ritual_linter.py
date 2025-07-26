"""Validation helpers for Sanctuary ritual invocation logs."""

import re
from typing import Dict


def validate_cast_spellform(log_line: str, glyph_reference: Dict[str, Dict]) -> bool:
    """Validates structure of ritual invocations."""
    if not log_line or not log_line.strip():
        return False

    if not re.match(r"^[a-zA-Z0-9_]+\(.*\)[.!?]$", log_line.strip()):
        return False

    glyphs = re.findall(r"[\U0001F300-\U0001FAFF]", log_line)
    for g in glyphs:
        if g not in glyph_reference:
            return False
    return True
