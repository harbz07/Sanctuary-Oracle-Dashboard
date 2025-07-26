"""Simple vector database utilities for the Sanctuary Codex."""

from __future__ import annotations

from typing import Dict, List, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class VectorDB:
    """Builds TF-IDF vectors for glyph data and enables similarity search."""

    def __init__(self, glyph_data: Dict[str, Dict]):
        self.glyphs: List[str] = list(glyph_data.keys())
        docs: List[str] = []
        for g in self.glyphs:
            info = glyph_data[g]
            parts = [
                info.get("literal", ""),
                info.get("affective", ""),
                " ".join(info.get("entities", [])),
            ]
            docs.append(" ".join(part for part in parts if part))
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(docs)

    def query(self, text: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Return glyphs ranked by similarity to the input text."""
        q_vec = self.vectorizer.transform([text])
        sims = cosine_similarity(q_vec, self.matrix)[0]
        ranked = sorted(zip(self.glyphs, sims), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]

    def neighbors(self, glyph: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Return glyphs similar to the provided glyph."""
        if glyph not in self.glyphs:
            return []
        idx = self.glyphs.index(glyph)
        g_vec = self.matrix[idx]
        sims = cosine_similarity(g_vec, self.matrix)[0]
        ranked = sorted(zip(self.glyphs, sims), key=lambda x: x[1], reverse=True)
        return [(g, s) for g, s in ranked if g != glyph][:top_k]


if __name__ == "__main__":
    from pathlib import Path
    from glyph_parser import parse_glyph_csv
    import pprint

    codex = parse_glyph_csv(Path("data/glyph_codex.csv"))
    vdb = VectorDB(codex)
    print("Query 'fire magic':")
    pprint.pprint(vdb.query("fire magic"))
    print("Neighbors for first glyph:")
    if vdb.glyphs:
        pprint.pprint(vdb.neighbors(vdb.glyphs[0]))
