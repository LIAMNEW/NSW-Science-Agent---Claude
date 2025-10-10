# src/tools/gemini_helper.py
from __future__ import annotations

import os
from typing import Optional
from dotenv import load_dotenv

import google.generativeai as genai


# Configure Gemini once per process
def _configure() -> None:
    # Load .env (GOOGLE_API_KEY=...)
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY is not set. Put it in a .env file at the project root like:\n"
            "GOOGLE_API_KEY=your_actual_key_here"
        )
    genai.configure(api_key=api_key)


_configured = False


def explain_with_gemini(prompt: str, model: str = "gemini-1.5-flash") -> str:
    """
    Simple wrapper that returns a short explanation string.
    """
    global _configured
    if not _configured:
        _configure()
        _configured = True

    m = genai.GenerativeModel(model)
    resp = m.generate_content(prompt)
    # The SDK returns the text in .text for simple generations
    return (resp.text or "").strip()
