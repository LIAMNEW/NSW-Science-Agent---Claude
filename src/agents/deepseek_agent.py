"""
DeepSeek Agent Base Class
Uses OpenAI-compatible API with custom base_url
"""
import os
from openai import OpenAI

class DeepSeekAgent:
    """Base class for agents using DeepSeek API"""
    
    def __init__(self, system_instruction="You are a helpful AI assistant."):
        """
        Initialize DeepSeek agent with system instruction
        
        Args:
            system_instruction: System prompt to guide the agent's behavior
        """
        self.system_instruction = system_instruction
        self.conversation_history = {}
        
        # Initialize DeepSeek client using OpenAI SDK
        api_key = os.getenv("API_DEEPSEEK")
        if not api_key:
            raise ValueError("API_DEEPSEEK environment variable not set")
        
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        
        print("✓ DeepSeek initialized")
    
    def generate_response(self, prompt, student_id="default", temperature=0.9, max_tokens=2048):
        """
        Generate a response using DeepSeek
        
        Args:
            prompt: User's question/prompt
            student_id: Student identifier for conversation history
            temperature: Creativity level (0.0-2.0)
            max_tokens: Maximum response length
            
        Returns:
            Generated response text
        """
        try:
            # Initialize conversation history for this student if needed
            if student_id not in self.conversation_history:
                self.conversation_history[student_id] = []
            
            # Build messages list
            messages = [
                {
                    "role": "system",
                    "content": self.system_instruction
                }
            ]
            
            # Add conversation history (last 3 exchanges)
            messages.extend(self.conversation_history[student_id][-6:])
            
            # Add current prompt
            messages.append({
                "role": "user",
                "content": prompt
            })
            
            # Call DeepSeek API
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=False
            )
            
            response_text = response.choices[0].message.content.strip()
            
            # Update conversation history
            self.conversation_history[student_id].append({
                "role": "user",
                "content": prompt
            })
            self.conversation_history[student_id].append({
                "role": "assistant",
                "content": response_text
            })
            
            # Keep only last 10 messages (5 exchanges)
            if len(self.conversation_history[student_id]) > 10:
                self.conversation_history[student_id] = self.conversation_history[student_id][-10:]
            
            return response_text
            
        except Exception as e:
            error_msg = f"Error generating DeepSeek response: {str(e)}"
            print(error_msg)
            return "I'm having trouble generating a response right now. Please try again in a moment."
    
    def clear_conversation(self, student_id="default"):
        """Clear conversation history for a student"""
        if student_id in self.conversation_history:
            self.conversation_history[student_id] = []
