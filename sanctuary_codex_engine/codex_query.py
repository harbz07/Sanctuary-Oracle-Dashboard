"""Codex semantic interface for querying glyphs and entities."""

from glyph_parser import parse_glyph_csv
from entity_linker import load_entity_registry, map_glyphs_to_entities


class CodexQuery:
    """Helper for exploring glyph and entity relationships."""

    def __init__(self, glyph_codex_path: str, entity_registry_path: str) -> None:
        self.glyphs = parse_glyph_csv(glyph_codex_path)
        self.entities = load_entity_registry(entity_registry_path)
        self.glyph_entity_map = map_glyphs_to_entities(self.glyphs, self.entities)

    def glyph_to_entities(self, glyph: str):
        """Return entities linked to a glyph."""
        return self.glyph_entity_map.get(glyph, [])

    def entity_to_glyphs(self, entity_name: str):
        """Return glyphs associated with an entity by name."""
        for entity in self.entities:
            if entity.get("name") == entity_name:
                return entity.get("glyphs", [])
        return []

    def list_all_glyphs(self):
        return list(self.glyphs.keys())

    def list_all_entities(self):
        return [e.get("name") for e in self.entities]

    def search_entities_by_essence(self, keyword: str):
        key = keyword.lower()
        return [e for e in self.entities if key in str(e.get("essence", "")).lower()]

    def glyph_cluster(self, glyph: str):
        """Find all glyphs that co-occur with the given glyph across entities."""
        co_glyphs = set()
        for entity in self.entities:
            glyphs = entity.get("glyphs", [])
            if glyph in glyphs:
                co_glyphs.update(glyphs)
        co_glyphs.discard(glyph)
        return list(co_glyphs)


if __name__ == "__main__":
    q = CodexQuery("data/glyph_codex.csv", "data/daemon_registry.json")
    print(q.glyph_to_entities("🜏"))
    print(q.entity_to_glyphs("Finalis"))
    print(q.search_entities_by_essence("becoming"))
    print(q.glyph_cluster("🜏"))

