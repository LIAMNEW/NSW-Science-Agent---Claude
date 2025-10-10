
# src/tools/utils.py
from typing import Dict, Any, List
import re

def detect_outcomes(user_query: str) -> Dict[str, List[str]]:
    """Very small keyword → NESA outcome mapping for demo."""
    q = user_query.lower()
    # Chemical World: mixtures
    if any(k in q for k in ["mixture", "separate", "solution", "filtration", "evaporation"]):
        return {"content_outcomes": ["SC4-SOL-01"], "ws_outcomes": ["SC4-WS-01", "SC4-WS-02"]}
    # Physical World: forces & motion
    if any(k in q for k in ["force", "motion", "speed", "acceleration", "net force"]):
        return {"content_outcomes": ["SC4-FOR-01"], "ws_outcomes": ["SC4-WS-02", "SC4-WS-05"]}
    # Living World: cells
    if any(k in q for k in ["cell", "microscope", "membrane", "organelle", "osmosis"]):
        return {"content_outcomes": ["SC4-CLS-01"], "ws_outcomes": ["SC4-WS-01", "SC4-WS-03"]}
    # Earth & Space: rock cycle
    if any(k in q for k in ["rock", "igneous", "sedimentary", "metamorphic", "rock cycle"]):
        return {"content_outcomes": ["SC4-EARTH-01"], "ws_outcomes": ["SC4-WS-01", "SC4-WS-04"]}
    return {"content_outcomes": [], "ws_outcomes": []}

def short_title(text: str, max_len: int = 80) -> str:
    if not text:
        return ""
    t = re.sub(r"\s+", " ", str(text)).strip()
    return t if len(t) <= max_len else t[: max_len - 1] + "…"
