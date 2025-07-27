"""Tools for detecting semantic drift between historical and current glyph data."""

from typing import Any, Dict, List


def detect_semantic_drift(glyph_history: Dict[str, Dict[str, Any]], current_codex: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Compares historical and current meanings of glyphs and flags shifts."""
    drift_results: List[Dict[str, Any]] = []
    for glyph, history in glyph_history.items():
        current = current_codex.get(glyph)
        if not current:
            continue
        literal_drift = history.get('literal') != current.get('literal')
        affective_drift = history.get('affective') != current.get('affective')
        if literal_drift or affective_drift:
            drift_results.append({
                'glyph': glyph,
                'literal_drift': literal_drift,
                'affective_drift': affective_drift,
                'history': history,
                'current': current,
            })
    return drift_results
