"""
Gemini Helper for NSW Science Agent
Provides generative AI capabilities using Google's Gemini API
"""
import os
from typing import Optional

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    print("google-generativeai not available, using fallback responses")


def configure_gemini():
    """Configure Gemini API with key from environment"""
    if not GENAI_AVAILABLE:
        return False
    
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        return True
    return False


def generate_explanation(
    topic: str,
    context: str = "",
    reading_level: str = "Year 7-8",
    max_tokens: int = 500
) -> str:
    """Generate a student-friendly explanation using Gemini"""
    
    if not GENAI_AVAILABLE or not configure_gemini():
        return f"""Let me explain {topic}:

This is a key concept in NSW Stage 4 Science. {context}

To understand this better:
• Think about real-world examples you see every day
• Practice using scientific methods to investigate
• Connect this to other science concepts you've learned

{topic} is important because it helps us understand how the natural world works!"""
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        prompt = f"""You are a NSW Stage 4 Science teacher explaining to {reading_level} students.

Topic: {topic}
Context: {context}

Provide a clear, engaging explanation that includes:
1. Simple definition (2-3 sentences)
2. Real-world analogy or example
3. One interesting fact
4. How this connects to NSW science curriculum

Keep it friendly, conversational, and appropriate for Years 7-8."""

        response = model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
        print(f"Gemini error: {e}")
        return f"Explanation for {topic}: This is an important science concept. {context}"
