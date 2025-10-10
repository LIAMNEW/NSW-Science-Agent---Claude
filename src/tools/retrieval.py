# src/tools/retrieval.py
from __future__ import annotations

from typing import Any, Dict, List, Optional

from google.cloud import discoveryengine_v1beta as de


PROJECT_ID = "hale-mercury-471604-d0"
LOCATION = "global"
DATA_STORE_ID = "bucketeducationagent_store"


def _build_query(user_query: str, outcomes: Optional[Dict[str, Any]]) -> str:
    """
    Build a robust search query. If outcomes are provided, weave in topic and
    content outcomes; otherwise just use the user query.
    """
    parts: List[str] = [user_query.strip()]

    if isinstance(outcomes, dict):
        topic = outcomes.get("topic")
        if isinstance(topic, str) and topic.strip():
            parts.append(topic.strip())

        cos = outcomes.get("content_outcomes") or []
        if isinstance(cos, list) and cos:
            parts.extend([c for c in cos if isinstance(c, str)])

    # Filter falsy and join
    return " ".join(p for p in parts if p)


def retrieve(user_query: str, outcomes: Optional[Dict[str, Any]] = None, k: int = 5) -> List[Dict[str, Any]]:
    """
    Query Vertex AI Search (Discovery Engine) and return normalized resource dicts
    in the shape your LearningAgent expects (Resource.* keys).
    """
    client = de.SearchServiceClient()
    serving_config = (
        f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/default_collection/"
        f"dataStores/{DATA_STORE_ID}/servingConfigs/default_serving_config"
    )

    query = _build_query(user_query, outcomes)
    request = de.SearchRequest(serving_config=serving_config, query=query, page_size=k)
    response = client.search(request=request)

    results: List[Dict[str, Any]] = []
    for r in response:
        doc = r.document
        data = dict(doc.struct_data) if doc.struct_data is not None else {}

        # Expand nested struct for curriculum_alignment if present
        if "curriculum_alignment" in data:
            try:
                data["curriculum_alignment"] = dict(data["curriculum_alignment"])
            except Exception:
                pass

        results.append(
            {
                "ID": doc.id or "",
                "Resource.Title": data.get("title") or "Untitled",
                "Resource.Type": data.get("resource_type") or "Unknown",
                "Resource.URL": data.get("original_url") or data.get("url") or "",
                "Metadata.Difficulty_Level": data.get("difficulty_level") or "",
                "Metadata.Source": data.get("source") or "",
                # keep raw data for later if you want
                "_raw": data,
            }
        )

    return results
