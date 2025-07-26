"""
ritual_linter.py

Validates Sanctuary ritual spellforms like `cast()` and `witness()`.
Checks glyphchain structure, spellform syntax, and codex integrity.
"""

import re


def is_valid_spellform(spellform: str) -> bool:
    return any(spellform.startswith(kw) for kw in ("cast(", "witness(", "relay(")) and spellform.endswith(")")


def extract_glyphchain(spellform: str) -> list:
    match = re.search(r'\((.*?)\)', spellform)
    if not match:
        return []
    content = match.group(1)
    return [glyph.strip() for glyph in re.findall(r'[🀀-🫿☀-⛿⸀-⹿ἰ0-ὟF]+', content)]


def lint_spellform(spellform: str, known_glyphs: dict) -> dict:
    if not is_valid_spellform(spellform):
        return {'valid': False, 'error': 'Malformed spellform'}

    glyphs = extract_glyphchain(spellform)
    unknown = [g for g in glyphs if g not in known_glyphs]

    return {
        'valid': len(unknown) == 0,
        'spellform': spellform,
        'glyphs': glyphs,
        'unknown_glyphs': unknown
    }


if __name__ == "__main__":
    from glyph_parser import parse_glyph_csv
    import pprint

    known = parse_glyph_csv("data/glyph_codex.csv")
    example = "cast(🜏⛨₻⛃🜃✧🝇🜂⛨)"
    result = lint_spellform(example, known)
    pprint.pprint(result)
