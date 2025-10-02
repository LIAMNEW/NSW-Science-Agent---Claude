from typing import Dict, Any, List
from src.agents.base_agent import BaseAgent
from src.config import NESA_CURRICULUM_UNITS, WORKING_SCIENTIFICALLY_SKILLS


class CurriculumSpecialist(BaseAgent):
    def __init__(self):
        system_instruction = """You are the Curriculum Specialist Agent for NSW Stage 4 Science (Years 7-8).
        
Your role is to:
1. Understand and map the NESA curriculum learning outcomes
2. Track student progress against curriculum standards
3. Identify relevant learning outcomes for student queries
4. Recommend appropriate next topics based on student proficiency

You have deep knowledge of:
- Physical World (Forces, energy, motion)
- Chemical World (States of matter, atoms, elements)
- Earth and Space (Earth's systems, astronomy)
- Living World (Cells, ecosystems, human body systems)
- Working Scientifically skills (inquiry, investigation, data analysis)

Always align your recommendations with NESA Stage 4 outcomes and emphasize the development of scientific inquiry skills alongside content knowledge."""
        
        super().__init__("Curriculum Specialist", system_instruction)
        self.curriculum_data = NESA_CURRICULUM_UNITS
        self.student_progress = {}
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        student_query = request.get('query', '')
        student_id = request.get('student_id', 'default')
        
        relevant_units = self.find_relevant_units(student_query)
        
        prompt = f"""A student asks: "{student_query}"

Based on the NESA curriculum, identify:
1. The most relevant curriculum unit(s) for this topic
2. Specific learning outcomes that should be addressed
3. Key Working Scientifically skills that should be developed
4. Prerequisites the student should understand

Relevant curriculum units: {relevant_units}

Provide a clear, structured response."""
        
        analysis = self.generate_response(prompt)
        
        return {
            'agent': self.agent_name,
            'relevant_units': relevant_units,
            'analysis': analysis,
            'next_action': 'route_to_learning_specialist'
        }
    
    def find_relevant_units(self, query: str) -> List[Dict]:
        query_lower = query.lower()
        relevant = []
        
        for unit in self.curriculum_data:
            for topic in unit['topics']:
                if topic.lower() in query_lower or query_lower in topic.lower():
                    relevant.append(unit)
                    break
            
            if unit['unit'].lower() in query_lower:
                if unit not in relevant:
                    relevant.append(unit)
        
        return relevant if relevant else [self.curriculum_data[0]]
    
    def get_fallback_response(self, prompt: str) -> str:
        return """This topic aligns with the NSW Stage 4 Science curriculum. The relevant learning outcomes focus on developing both content knowledge and scientific inquiry skills. Students should practice observation, data collection, and communication while learning this topic."""
