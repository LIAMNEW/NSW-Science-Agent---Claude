from abc import ABC, abstractmethod
from typing import Dict, Any, List
from src.config import PROJECT_ID, LOCATION, MODEL_NAME

try:
    import vertexai
    from vertexai.generative_models import GenerativeModel, Part, Content
    VERTEX_AI_AVAILABLE = True
except Exception as e:
    print(f"Vertex AI not available: {e}")
    print("Running in demo mode with simulated responses.")
    VERTEX_AI_AVAILABLE = False


class BaseAgent(ABC):
    def __init__(self, agent_name: str, system_instruction: str):
        self.agent_name = agent_name
        self.system_instruction = system_instruction
        self.model = None
        self.chat_session = None
        self.initialize_model()
    
    def initialize_model(self):
        if not VERTEX_AI_AVAILABLE:
            print(f"Vertex AI not available for {self.agent_name}. Running in demo mode.")
            return
        
        try:
            vertexai.init(project=PROJECT_ID, location=LOCATION)
            self.model = GenerativeModel(
                model_name=MODEL_NAME,
                system_instruction=self.system_instruction
            )
            self.chat_session = self.model.start_chat()
        except Exception as e:
            print(f"Warning: Could not initialize Vertex AI for {self.agent_name}: {e}")
            print("The system will operate in demo mode with simulated responses.")
    
    @abstractmethod
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    def generate_response(self, prompt: str) -> str:
        if self.chat_session:
            try:
                response = self.chat_session.send_message(prompt)
                return response.text
            except Exception as e:
                print(f"Error generating response from {self.agent_name}: {e}")
                return self.get_fallback_response(prompt)
        else:
            return self.get_fallback_response(prompt)
    
    @abstractmethod
    def get_fallback_response(self, prompt: str) -> str:
        pass
