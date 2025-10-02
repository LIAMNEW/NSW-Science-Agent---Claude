from typing import Dict, Any, List
from src.agents.base_agent import BaseAgent


class LearningSpecialist(BaseAgent):
    def __init__(self):
        system_instruction = """You are the Learning Specialist Agent for NSW Stage 4 Science (Years 7-8).

Your role is to:
1. Create engaging lesson plans and learning pathways
2. Explain scientific concepts clearly and age-appropriately
3. Recommend relevant learning resources (videos, simulations, readings)
4. Break down complex topics into manageable chunks
5. Adapt explanations based on student understanding level

Your teaching style should be:
- Engaging and conversational (act as a friendly learning buddy)
- Use analogies and real-world examples
- Encourage curiosity and questioning
- Connect concepts to everyday life
- Support diverse learning styles

Always emphasize hands-on learning and scientific inquiry alongside theoretical knowledge."""
        
        super().__init__("Learning Specialist", system_instruction)
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        topic = request.get('topic', '')
        curriculum_context = request.get('curriculum_context', {})
        student_level = request.get('level', 'beginner')
        
        prompt = f"""Create an engaging learning session for: {topic}

Context from curriculum: {curriculum_context}
Student level: {student_level}

Provide:
1. A clear, friendly explanation of the main concepts
2. Real-world examples or analogies
3. Suggested hands-on activities or experiments
4. Questions to encourage critical thinking
5. Connections to other science topics

Make it engaging and appropriate for Years 7-8 students."""
        
        lesson_content = self.generate_response(prompt)
        
        recommended_resources = self.recommend_resources(topic)
        
        return {
            'agent': self.agent_name,
            'lesson_content': lesson_content,
            'resources': recommended_resources,
            'next_action': 'present_to_student'
        }
    
    def recommend_resources(self, topic: str) -> List[Dict]:
        resources = []
        topic_lower = topic.lower()
        
        if 'force' in topic_lower or 'motion' in topic_lower:
            resources.extend([
                {'type': 'video', 'title': 'Forces and Motion Explained', 'source': 'Khan Academy'},
                {'type': 'simulation', 'title': 'Forces Virtual Lab', 'source': 'PhET Interactive'},
            ])
        elif 'cell' in topic_lower:
            resources.extend([
                {'type': 'video', 'title': 'Introduction to Cells', 'source': 'Crash Course'},
                {'type': 'simulation', 'title': 'Using a Light Microscope', 'source': 'LabXchange'},
            ])
        elif 'rock' in topic_lower or 'mineral' in topic_lower:
            resources.extend([
                {'type': 'video', 'title': 'Rock Cycle Explained', 'source': 'Science with Skilldog'},
                {'type': 'resource', 'title': 'Earth Science 101', 'source': 'Geoscience Australia'},
            ])
        elif 'energy' in topic_lower:
            resources.extend([
                {'type': 'video', 'title': 'Types of Energy', 'source': 'Bozeman Science'},
                {'type': 'simulation', 'title': 'Energy Transfer Simulation', 'source': 'PhET Interactive'},
            ])
        else:
            resources.append({
                'type': 'video', 
                'title': f'{topic} - Science Explained', 
                'source': 'Educational YouTube Channels'
            })
        
        return resources
    
    def get_fallback_response(self, prompt: str) -> str:
        return """Let me help you understand this topic! This concept is fascinating because it relates to things you see every day. I'll break it down into simple steps, and we'll explore it together through examples and activities. Remember, science is all about asking questions and discovering answers through observation and experimentation!"""
