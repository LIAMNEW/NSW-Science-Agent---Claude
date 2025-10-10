# src/tools/llm.py
from __future__ import annotations
import os
from typing import Optional, Dict, Any, List
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting

# Defaults: use same as your Discovery Engine region
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "hale-mercury-471604-d0")
LOCATION = os.getenv("VERTEX_LOCATION", "global")

# Use a generally available Gemini model via Vertex AI
# If "gemini-1.5-flash" is unavailable in your region, try "gemini-1.0-pro" or "gemini-1.5-pro".
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

_model: Optional[GenerativeModel] = None

def get_model() -> GenerativeModel:
    global _model
    if _model is None:
        vertexai.init(project=PROJECT_ID, location=LOCATION)
        _model = GenerativeModel(MODEL_NAME)
    return _model

# Basic, teacher-safe settings (you can tune these later)
SAFETY = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUAL_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
]

def generate_text(prompt: str, system_instruction: Optional[str] = None) -> str:
    """
    Simple wrapper to call Gemini and return text.
    """
    model = get_model()
    if system_instruction:
        model = GenerativeModel(MODEL_NAME, system_instruction=system_instruction)

    resp = model.generate_content(
        prompt,
        safety_settings=SAFETY,
        generation_config={
            "temperature": 0.6,
            "top_p": 0.9,
            "top_k": 40,
            "max_output_tokens": 800,
        },
    )
    # Vertex SDK returns .text on a friendly wrapper
    return getattr(resp, "text", "").strip()
