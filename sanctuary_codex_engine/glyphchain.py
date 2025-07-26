"""Utilities for parsing and scoring glyphchains."""

from typing import Dict, List

import re

GLYPH_RE = re.compile(r"[🀀-🫿☀-⛿⸀-⹿ἰ0-ὟF]+")


def parse_chain(text: str) -> List[str]:
    """Extract glyphs from a glyphchain string."""
    return GLYPH_RE.findall(text)


def score_chain(glyphs: List[str], known_glyphs: Dict[str, Dict]) -> float:
    """Score a glyphchain by fraction of glyphs present in the codex."""
    if not glyphs:
        return 0.0
    known = sum(1 for g in glyphs if g in known_glyphs)
    return known / len(glyphs)


if __name__ == "__main__":
    from pathlib import Path
    from glyph_parser import parse_glyph_csv
    import pprint

    codex = parse_glyph_csv(Path("data/glyph_codex.csv"))
    sample = "🜏⛨₻⛃🜃✧🝇🜂⛨"
    glyphs = parse_chain(sample)
    pprint.pprint(glyphs)
    print(score_chain(glyphs, codex))

