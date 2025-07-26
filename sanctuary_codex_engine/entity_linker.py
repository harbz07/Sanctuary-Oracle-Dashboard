from typing import Dict, List, Any


def map_glyphs_to_entities(glyph_data: Dict[str, Dict[str, Any]], entity_registry: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Connects each glyph to matching or suggested entities from registry."""
    mapping: Dict[str, List[Dict[str, Any]]] = {}
    for glyph, info in glyph_data.items():
        mapping[glyph] = []
        glyph_entities = [e.lower() for e in info.get('entities', [])]
        for entity in entity_registry:
            name = entity.get('name', '').lower()
            if not name:
                continue
            if name in glyph_entities or any(name in ge for ge in glyph_entities):
                mapping[glyph].append(entity)
    return mapping
