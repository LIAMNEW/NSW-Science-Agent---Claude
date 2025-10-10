# src/tools/explainer.py
"""
Gemini Explanation Helper for NSW Science Agent
-----------------------------------------------
Generates short, student-friendly explanations using Gemini via Vertex AI.
Reads API key from GOOGLE_API_KEY (preferred) or uses ADC if running on GCP.
"""

from __future__ import annotations
import os
from typing import Dict, Any, Optional

try:
    # For API key direct auth
    import google.generativeai as genai
    USE_API_KEY = True
except ImportError:
    # Fallback to Vertex AI SDK
    from vertexai import init
    from vertexai.generative_models import GenerativeModel
    USE_API_KEY = False


def _init_model():
    """
    Initialize a Gemini model either with google-generativeai (API key)
    or Vertex AI Python SDK (ADC).
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    project = os.getenv("GOOGLE_CLOUD_PROJECT", "hale-mercury-471604-d0")
    location = os.getenv("VERTEX_LOCATION", "global")

    if USE_API_KEY and api_key:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel("gemini-1.5-flash")
    else:
        # ADC via Vertex AI
        init(project=project, location=location)
        return GenerativeModel("gemini-1.5-flash")


def generate_explanation(
    topic: str,
    outcomes: Dict[str, Any],
    reading_level: str = "Year 7",
) -> Optional[str]:
    """
    Produce a brief, NSW Stage 4–aligned explanation.
    """
    try:
        model = _init_model()

        co = ", ".join(outcomes.get("content_outcomes", [])) or "Stage 4 outcomes"
        ws = ", ".join(outcomes.get("ws_outcomes", [])) or "WS skills"

        prompt = f"""
You are a NSW Stage 4 Science teacher. Explain the concept of **{topic}** for a {reading_level} student.
Use NSW syllabus language. Include:
• a clear, simple explanation (4–6 sentences)
• one real-world analogy
• one worked example or short check question + answer
• one WS (Working Scientifically) skill students will practise

Content Outcomes: {co}
WS Outcomes: {ws}
"""

        if USE_API_KEY and os.getenv("GOOGLE_API_KEY"):
            resp = model.generate_content(prompt)
            return resp.text.strip()
        else:
            resp = model.generate_content(prompt)
            return getattr(resp, "text", "").strip()
    except Exception as e:
        return f"(Gemini explanation unavailable: {e})"
