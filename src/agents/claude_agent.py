"""
Claude-powered Agent Base Class
Uses Anthropic's Claude API for conversational AI capabilities
"""
import os
from typing import Dict, Any, Optional
from abc import ABC, abstractmethod

try:
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("anthropic package not available")


class ClaudeAgent(ABC):
    """Base class for agents using Claude API"""
    
    def __init__(self, agent_name: str, system_instruction: str):
        self.agent_name = agent_name
        self.system_instruction = system_instruction
        self.client = None
        self.conversation_history = []
        self.initialize_model()
    
    def initialize_model(self):
        """Initialize Claude client with API key"""
        if not ANTHROPIC_AVAILABLE:
            print(f"Claude not available for {self.agent_name}. Using fallback mode.")
            return
        
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print(f"No Claude API key found for {self.agent_name}. Using fallback mode.")
            return
        
        try:
            self.client = Anthropic(api_key=api_key)
            print(f"✓ Claude initialized for {self.agent_name}")
            
        except Exception as e:
            print(f"Error initializing Claude for {self.agent_name}: {e}")
            self.client = None
    
    @abstractmethod
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Process incoming request - to be implemented by subclass"""
        pass
    
    def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate a response using Claude with conversation context"""
        
        full_prompt = prompt
        if context:
            full_prompt = f"{context}\n\n{prompt}"
        
        if self.client:
            try:
                # Build messages for Claude API
                messages = self.conversation_history.copy()
                messages.append({
                    "role": "user",
                    "content": full_prompt
                })
                
                # Call Claude API - Using Haiku for speed and availability
                response = self.client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=2048,
                    temperature=0.9,
                    system=self.system_instruction,
                    messages=messages
                )
                
                response_text = response.content[0].text.strip()
                
                # Update conversation history
                self.conversation_history.append({
                    "role": "user",
                    "content": full_prompt
                })
                self.conversation_history.append({
                    "role": "assistant",
                    "content": response_text
                })
                
                # Keep only last 10 messages (5 exchanges)
                if len(self.conversation_history) > 10:
                    self.conversation_history = self.conversation_history[-10:]
                
                return response_text
                
            except Exception as e:
                print(f"Error generating Claude response from {self.agent_name}: {e}")
                return self.get_fallback_response(prompt)
        else:
            return self.get_fallback_response(prompt)
    
    @abstractmethod
    def get_fallback_response(self, prompt: str) -> str:
        """Fallback response when Claude is unavailable - to be implemented by subclass"""
        pass
    
    def reset_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []
