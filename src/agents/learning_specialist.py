from typing import Dict, Any, List
from src.agents.base_agent import BaseAgent
from src.tools.resource_manager import (
    load_resource_catalog, 
    find_resources_by_query, 
    get_youtube_videos,
    find_resources_by_type,
    format_resource_for_display
)
from src.tools.gemini_helper import generate_explanation


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
        self.resource_catalog = load_resource_catalog()
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        topic = request.get('topic', '')
        curriculum_context = request.get('curriculum_context', {})
        student_level = request.get('level', 'beginner')
        available_resources = request.get('available_resources', [])
        
        # Generate AI-powered explanation
        ai_explanation = generate_explanation(
            topic=topic,
            context=str(curriculum_context),
            reading_level="Year 7-8"
        )
        
        # Find comprehensive resources from catalog
        query_resources = find_resources_by_query(topic, self.resource_catalog)
        youtube_videos = get_youtube_videos(topic, self.resource_catalog)
        simulations = find_resources_by_type("Interactive Simulation", self.resource_catalog)
        simulations = [s for s in simulations if topic.lower() in s.get('Resource.Title', '').lower() or 
                       topic.lower() in s.get('Metadata.Description', '').lower()]
        
        prompt = f"""Create an engaging learning session for: {topic}

Context: {curriculum_context}
Student level: {student_level}

Available resources:
- {len(youtube_videos)} YouTube videos
- {len(simulations)} interactive simulations
- {len(query_resources)} total educational resources

Provide:
1. A clear, friendly explanation of the main concepts
2. Real-world examples or analogies
3. Suggested hands-on activities or experiments
4. Questions to encourage critical thinking
5. Connections to other science topics

Make it engaging and appropriate for Years 7-8 students."""
        
        lesson_content = self.generate_response(prompt) if not ai_explanation.startswith("Let me explain") else ai_explanation
        
        # Format all resources for display
        all_resources = []
        all_resources.extend([format_resource_for_display(v) for v in youtube_videos[:3]])
        all_resources.extend([format_resource_for_display(s) for s in simulations[:3]])
        all_resources.extend([format_resource_for_display(r) for r in query_resources[:4]])
        
        return {
            'agent': self.agent_name,
            'lesson_content': lesson_content,
            'resources': all_resources,
            'youtube_videos': [format_resource_for_display(v) for v in youtube_videos[:5]],
            'simulations': [format_resource_for_display(s) for s in simulations[:3]],
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
