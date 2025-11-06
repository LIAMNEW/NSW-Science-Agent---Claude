from typing import Dict, Any, List
import random
from src.agents.gemini_agent import GeminiAgent
from src.tools.resource_manager import (
    load_resource_catalog, 
    find_resources_by_query, 
    get_youtube_videos,
    find_resources_by_type,
    format_resource_for_display
)
from src.tools.gemini_helper import generate_explanation
from src.data.nesa_official_content import get_nesa_teaching_content
from src.tools.textbook_manager import get_textbook_manager


class LearningSpecialist(GeminiAgent):
    def __init__(self):
        system_instruction = """You are Nova, the Learning Specialist - an enthusiastic, expert science educator for NSW Stage 4 students (Years 7-8).

🎯 YOUR PERSONALITY:
You're that teacher everyone wishes they had - passionate about science, genuinely excited to share knowledge, and skilled at making complex ideas click. You're approachable, creative, and adapt your teaching style to each student's needs.

💬 YOUR CONVERSATION STYLE:
- Natural, conversational language - not textbook-y or stiff
- Vary your openings and transitions - never sound formulaic
- Match student energy (curious = enthusiastic, confused = patient & clarifying)
- Use "you" and "we" to create collaborative learning
- Strategic emoji use for engagement (🔬🌟💡 etc.) but don't overdo it
- Analogies from student life (games, sports, social media, daily experiences)
- Ask thought-provoking questions to deepen understanding
- Reference real scientists, discoveries, and current events when relevant

🌟 YOUR TEACHING APPROACH:
1. **Engage First**: Hook students with an interesting fact, question, or real-world connection
2. **Explain Clearly**: Break concepts into digestible pieces using analogies and examples
3. **Hands-On Focus**: Emphasize NESA investigations and practical applications
4. **Connect Ideas**: Link to prior knowledge, other topics, and real-world uses
5. **Encourage Inquiry**: Foster curiosity with open-ended questions
6. **Multiple Pathways**: Offer different ways to understand (visual, hands-on, conceptual)

✨ RESPONSE VARIATION RULES:
- NEVER use identical lesson openings ("Today we'll learn about...")
- Vary explanation approaches - use different analogies each time
- Mix up your teaching methods (story-telling, questioning, demonstration, discovery)
- Adapt complexity based on student responses
- Reference NESA investigations naturally, not mechanically

🔬 NSW STAGE 4 EXPERTISE:
- You know all 8 focus areas deeply: Forces, Cells, Universe, Solutions, Living Systems, Atoms, Change, Data Science
- You integrate Working Scientifically skills naturally into lessons
- You use authentic NESA investigations and outcomes
- You connect to Australian context and Aboriginal/Torres Strait Islander science

🚫 AVOID:
- Robotic, repetitive lesson structures
- Dense paragraphs of text - break it up!
- Overly technical jargon without explanation
- Generic, boring examples
- Sounding like you're reading from a syllabus

Remember: You're not just delivering content - you're sparking curiosity and building confident, scientifically-literate young people!"""
        
        super().__init__("Learning Specialist", system_instruction)
        self.resource_catalog = load_resource_catalog()
        self.textbook_manager = get_textbook_manager()
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        topic = request.get('topic', '')
        curriculum_context = request.get('curriculum_context', {})
        student_level = request.get('level', 'beginner')
        available_resources = request.get('available_resources', [])
        
        # Get official NESA teaching content
        nesa_content = get_nesa_teaching_content(topic)
        investigations = nesa_content.get('investigations', [])
        key_ideas = nesa_content.get('key_ideas', [])
        teaching_focus = nesa_content.get('teaching_focus', '')
        
        # Find comprehensive resources from catalog
        query_resources = find_resources_by_query(topic, self.resource_catalog)
        youtube_videos = get_youtube_videos(topic, self.resource_catalog)
        simulations = find_resources_by_type("Interactive Simulation", self.resource_catalog)
        simulations = [s for s in simulations if topic.lower() in s.get('Resource.Title', '').lower() or 
                       topic.lower() in s.get('Metadata.Description', '').lower()]
        
        # Build prompt with NESA investigations
        investigations_text = '\n'.join(f'• {inv}' for inv in investigations[:3]) if investigations else ''
        
        prompt = f"""A Year 7-8 student wants to learn about: {topic}

🎯 NESA Context:
Teaching Focus: {teaching_focus}

Key Ideas: {', '.join(key_ideas[:3])}

🔬 Hands-On Options:
{investigations_text}

📚 Resources Available: {len(youtube_videos)} videos, {len(simulations)} simulations

Your Mission:
Create an engaging, conversational learning experience (not a formal lesson plan). 

Start with a hook - something surprising, a question, or a real-world connection. Then explain the key concepts using relatable analogies. Naturally weave in one of the NESA investigations as something students could try. End with a thought-provoking question.

Keep it:
- Conversational and friendly (not textbook-y)
- Broken into digestible chunks
- Rich with examples from student life
- About 200-300 words

Remember: You're Nova, their enthusiastic learning buddy, not a formal teacher!"""
        
        lesson_content = self.generate_response(prompt)
        
        # Get textbook recommendations
        textbook_recommendations = self.textbook_manager.search_textbooks(topic)
        
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
            'textbook_recommendations': textbook_recommendations,
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
        """Provide varied, engaging fallback responses"""
        responses = [
            "Ooh, great topic! 🌟 You know what's cool about this? It's happening all around you right now. Let me break it down with some examples from everyday life. Think about [pause for effect] - ever noticed how...? That's this concept in action! Science isn't just in textbooks - it's in everything we do.",
            
            "This is one of my favorite things to explain! 💡 Here's a way to think about it that might click: imagine... [uses analogy]. Sound familiar? That's basically what's happening at a scientific level. Pretty neat, right? Let's dig deeper into how this works.",
            
            "Alright, let's make this super clear! 🔬 The key idea here is... and here's why it matters: you've probably experienced this yourself without even realizing it. Ever wondered why...? That's exactly what we're talking about! Science is all about connecting the dots between what we observe and why it happens.",
            
            "I love this question! 😊 So here's the thing - this concept might sound complex, but it's actually pretty intuitive once you see it in action. Think about when you... [everyday example]. That's the same principle! Let me walk you through the science behind what's happening.",
            
            "Great choice of topic! 🎯 You're about to understand something that explains so much of the world around you. The basic idea is... and what makes this really interesting is how it shows up everywhere - from your phone to the weather outside. Let's explore this step by step!",
        ]
        return random.choice(responses)
