"""
Gemini-powered Agent Base Class
Uses Google's Gemini API for conversational AI capabilities
"""
import os
from typing import Dict, Any, Optional
from abc import ABC, abstractmethod

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    print("google-generativeai not available")


class GeminiAgent(ABC):
    """Base class for agents using Gemini API"""
    
    def __init__(self, agent_name: str, system_instruction: str):
        self.agent_name = agent_name
        self.system_instruction = system_instruction
        self.model = None
        self.chat_session = None
        self.conversation_history = []
        self.initialize_model()
    
    def initialize_model(self):
        """Initialize Gemini model with API key"""
        if not GENAI_AVAILABLE:
            print(f"Gemini not available for {self.agent_name}. Using fallback mode.")
            return
        
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print(f"No Gemini API key found for {self.agent_name}. Using fallback mode.")
            return
        
        try:
            genai.configure(api_key=api_key)
            
            generation_config = {
                "temperature": 0.9,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 1024,
            }
            
            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            ]
            
            self.model = genai.GenerativeModel(
                model_name="gemini-2.0-flash",
                generation_config=generation_config,
                safety_settings=safety_settings,
                system_instruction=self.system_instruction
            )
            
            self.chat_session = self.model.start_chat(history=[])
            print(f"✓ Gemini initialized for {self.agent_name}")
            
        except Exception as e:
            print(f"Error initializing Gemini for {self.agent_name}: {e}")
            self.model = None
            self.chat_session = None
    
    @abstractmethod
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Process incoming request - to be implemented by subclass"""
        pass
    
    def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate a response using Gemini with conversation context"""
        
        full_prompt = prompt
        if context:
            full_prompt = f"{context}\n\n{prompt}"
        
        if self.chat_session:
            try:
                response = self.chat_session.send_message(full_prompt)
                response_text = response.text.strip()
                
                self.conversation_history.append({
                    "role": "user",
                    "content": prompt
                })
                self.conversation_history.append({
                    "role": "assistant",
                    "content": response_text
                })
                
                if len(self.conversation_history) > 10:
                    self.conversation_history = self.conversation_history[-10:]
                
                return response_text
                
            except Exception as e:
                print(f"Error generating Gemini response from {self.agent_name}: {e}")
                return self.get_fallback_response(prompt)
        else:
            return self.get_fallback_response(prompt)
    
    @abstractmethod
    def get_fallback_response(self, prompt: str) -> str:
        """Fallback response when Gemini is unavailable - to be implemented by subclass"""
        pass
    
    def reset_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []
        if self.chat_session and self.model:
            self.chat_session = self.model.start_chat(history=[])
