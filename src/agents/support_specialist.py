from typing import Dict, Any
from src.agents.base_agent import BaseAgent


class SupportSpecialist(BaseAgent):
    def __init__(self):
        system_instruction = """You are the Support Specialist Agent - a friendly learning buddy for NSW Stage 4 Science students (Years 7-8).

Your role is to:
1. Provide emotional support and encouragement
2. Help struggling students by breaking down complex concepts
3. Find alternative explanations and resources when students don't understand
4. Connect science to real-world applications and careers
5. Maintain motivation and curiosity about science
6. Provide context and background when needed

Your personality should be:
- Warm, friendly, and encouraging (like a supportive friend)
- Patient and understanding
- Enthusiastic about science
- Empathetic to learning challenges
- Inspiring and motivating

Always:
- Celebrate effort and progress, not just correctness
- Provide multiple ways to understand concepts
- Share interesting real-world connections
- Encourage questions and curiosity
- Build confidence in scientific thinking"""
        
        super().__init__("Support Specialist", system_instruction)
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        support_type = request.get('type', 'general')
        context = request.get('context', '')
        student_message = request.get('message', '')
        
        if support_type == 'struggling':
            return self.provide_remedial_support(context, student_message)
        elif support_type == 'motivation':
            return self.provide_encouragement(context)
        elif support_type == 'career_connection':
            return self.connect_to_careers(context)
        else:
            return self.provide_general_support(student_message)
    
    def provide_remedial_support(self, topic: str, student_concern: str) -> Dict[str, Any]:
        prompt = f"""A student is struggling with: {topic}

They said: "{student_concern}"

As a supportive learning buddy:
1. Acknowledge their feelings and effort
2. Break down the concept into simpler steps
3. Provide a different explanation or analogy
4. Suggest alternative learning approaches
5. Offer encouragement and next steps

Be warm, patient, and helpful."""
        
        support_message = self.generate_response(prompt)
        
        return {
            'agent': self.agent_name,
            'support_message': support_message,
            'next_action': 'provide_alternative_resources'
        }
    
    def provide_encouragement(self, context: str) -> Dict[str, Any]:
        prompt = f"""Provide motivational support for a student learning about: {context}

Include:
1. Encouragement about their learning journey
2. An interesting fact or real-world application
3. Why this topic matters
4. Confidence-building message

Be enthusiastic and inspiring!"""
        
        encouragement = self.generate_response(prompt)
        
        return {
            'agent': self.agent_name,
            'encouragement': encouragement
        }
    
    def connect_to_careers(self, topic: str) -> Dict[str, Any]:
        prompt = f"""Connect the topic "{topic}" to real-world careers and applications.

Share:
1. Interesting careers that use this science
2. How this knowledge is applied in the real world
3. Current scientific developments in this area
4. How students can explore this field further

Make it exciting and relatable!"""
        
        career_info = self.generate_response(prompt)
        
        return {
            'agent': self.agent_name,
            'career_connections': career_info
        }
    
    def provide_general_support(self, message: str) -> Dict[str, Any]:
        prompt = f"""A student says: "{message}"

Respond as a friendly, supportive learning buddy. Be helpful, encouraging, and relate to their interests in science."""
        
        response = self.generate_response(prompt)
        
        return {
            'agent': self.agent_name,
            'response': response
        }
    
    def get_fallback_response(self, prompt: str) -> str:
        return """Hey! I'm here to help you out. Science can seem tricky sometimes, but you're doing great by asking questions and staying curious! Let's break this down together into smaller pieces. Remember, every scientist started exactly where you are now - learning step by step. You've got this! What specific part would you like to explore first?"""
