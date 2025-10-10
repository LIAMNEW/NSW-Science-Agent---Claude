# src/tools/vertex_helper.py
from __future__ import annotations

from typing import Optional

import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting, HarmCategory, Part

# Choose a Vertex AI region that supports Gemini. us-central1 is the safest bet.
_DEFAULT_LOCATION = "us-central1"

# You already set the project with gcloud; but we allow overriding in code if needed.
def _ensure_vertex_init(project_id: Optional[str] = None, location: Optional[str] = None) -> None:
    vertexai.init(
        project=project_id,         # None -> uses gcloud config
        location=location or _DEFAULT_LOCATION,
    )

def explain_with_vertex(
    prompt: str,
    *,
    project_id: Optional[str] = None,
    location: Optional[str] = None,
    model_name: str = "gemini-1.5-flash-002",
    max_output_tokens: int = 512,
    temperature: float = 0.4,
) -> str:
    """
    Call Gemini on Vertex AI with ADC (no API key needed).
    """
    _ensure_vertex_init(project_id, location)

    model = GenerativeModel(model_name)

    safety = [
        SafetySetting(HarmCategory.HARM_CATEGORY_HARASSMENT, SafetySetting.HarmBlockThreshold.BLOCK_NONE),
        SafetySetting(HarmCategory.HARM_CATEGORY_HATE_SPEECH, SafetySetting.HarmBlockThreshold.BLOCK_NONE),
        SafetySetting(HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, SafetySetting.HarmBlockThreshold.BLOCK_NONE),
        SafetySetting(HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, SafetySetting.HarmBlockThreshold.BLOCK_NONE),
    ]

    resp = model.generate_content(
        [Part.from_text(prompt)],
        generation_config={"max_output_tokens": max_output_tokens, "temperature": temperature},
        safety_settings=safety,
    )
    return (resp.text or "").strip()
