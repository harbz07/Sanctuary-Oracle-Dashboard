import csv
from typing import Dict, List

def parse_glyph_csv(file_path: str) -> Dict[str, Dict[str, List[str]]]:
    """Parses glyph encyclopedia into a structured dictionary keyed by glyph."""
    glyphs: Dict[str, Dict[str, List[str]]] = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            glyph = row.get('glyph') or row.get('symbol')
            if not glyph:
                continue
            entities = row.get('entities') or ''
            entities_list = [e.strip() for e in entities.split(';') if e.strip()]
            glyphs[glyph] = {
                'literal': row.get('literal', '').strip(),
                'affective': row.get('affective', '').strip(),
                'entities': entities_list,
            }
    return glyphs
