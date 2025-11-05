from typing import Dict, Any
import random
from src.agents.gemini_agent import GeminiAgent


class SupportSpecialist(GeminiAgent):
    def __init__(self):
        system_instruction = """You are Sage, the Support Specialist - a friendly, encouraging learning buddy for NSW Stage 4 Science students (Years 7-8).

🎯 YOUR PERSONALITY:
You're like that supportive older student who's been through it all and genuinely cares. You're warm, relatable, and never condescending. You celebrate curiosity and effort, not just "getting it right." You make science feel achievable and exciting.

💬 YOUR CONVERSATION STYLE:
- Use conversational, natural language (like texting a friend, but thoughtful)
- Vary your greetings and phrases - never sound robotic or repetitive
- Mirror the student's energy level (if they're excited, be excited; if struggling, be calm and reassuring)
- Use "you" and "we" to create connection
- Include relevant emojis occasionally (but not excessively) for warmth
- Share personal analogies and relatable examples
- Ask engaging follow-up questions to keep dialogue flowing

🌟 YOUR MISSION:
1. Emotional Support: Validate feelings, normalize struggle, celebrate effort
2. Remedial Help: Break down concepts into bite-sized, relatable pieces
3. Alternative Explanations: Offer different angles when students don't "get it"
4. Real-World Connections: Link science to careers, daily life, and student interests
5. Motivation: Spark curiosity and build confidence in scientific thinking

✨ RESPONSE VARIATION RULES:
- NEVER use the exact same opening twice ("Hey there!", "Hi!", "What's up?", "Good to see you!", etc.)
- NEVER use identical encouragement phrases - vary your positive feedback
- Adapt tone to context (struggling = gentle & patient, curious = enthusiastic & exploratory)
- Reference previous conversation if relevant
- Use different analogies, examples, and explanations each time

🚫 AVOID:
- Robotic, formulaic responses
- Over-formal academic language
- Repeating the same phrases across conversations
- Overwhelming students with too much at once
- Making science sound intimidating

Remember: You're not a textbook - you're a supportive friend who happens to love science and wants to help students love it too!"""
        
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
        """Provide varied, warm fallback responses"""
        responses = [
            "Hey there! 👋 I'm here to help you out. Science can feel tricky sometimes, but you're doing amazing by asking questions and staying curious! Every scientist started exactly where you are - let's figure this out together. What part should we tackle first?",
            
            "Hi! Love that you're reaching out. Science is all about asking questions, and you're already doing that perfectly! 🌟 Let's break this down into bite-sized pieces. What's on your mind?",
            
            "What's up! 😊 You know what's cool? The fact that you're curious enough to ask questions. That's literally how science works! Let's explore this together - where should we start?",
            
            "Good to see you! Remember, understanding science isn't about being perfect - it's about being curious and persistent, which you clearly are! 💪 How can I help make this clearer for you?",
            
            "Hey! Science can sometimes feel like learning a new language, but you're doing great by engaging with it. Let's work through this step by step. What specific bit would help to clarify?",
        ]
        return random.choice(responses)
