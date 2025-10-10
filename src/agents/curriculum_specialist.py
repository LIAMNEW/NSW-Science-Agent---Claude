from typing import Dict, Any, List
from src.agents.base_agent import BaseAgent
from src.config import NESA_CURRICULUM_UNITS, WORKING_SCIENTIFICALLY_SKILLS
from src.tools.resource_manager import load_resource_catalog, find_resources_by_unit, find_resources_by_query
from src.tools.utils import detect_outcomes


class CurriculumSpecialist(BaseAgent):
    def __init__(self):
        system_instruction = """You are the Curriculum Specialist Agent for NSW Stage 4 Science (Years 7-8).
        
Your role is to:
1. Understand and map the NESA curriculum learning outcomes
2. Track student progress against curriculum standards
3. Identify relevant learning outcomes for student queries
4. Recommend appropriate next topics based on student proficiency
5. Connect queries to appropriate educational resources

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
        self.resource_catalog = load_resource_catalog()
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        student_query = request.get('query', '')
        student_id = request.get('student_id', 'default')
        
        # Find relevant curriculum units
        relevant_units = self.find_relevant_units(student_query)
        
        # Detect NESA outcomes from query
        outcomes = detect_outcomes(student_query)
        
        # Find matching resources
        available_resources = find_resources_by_query(student_query, self.resource_catalog)
        
        prompt = f"""A student asks: "{student_query}"

Based on the NESA curriculum, identify:
1. The most relevant curriculum unit(s) for this topic
2. Specific learning outcomes that should be addressed
3. Key Working Scientifically skills that should be developed
4. Prerequisites the student should understand

Relevant curriculum units: {relevant_units}
Detected outcomes: {outcomes}
Available educational resources: {len(available_resources)} resources found

Provide a clear, structured response that guides the learning journey."""
        
        analysis = self.generate_response(prompt)
        
        return {
            'agent': self.agent_name,
            'relevant_units': relevant_units,
            'outcomes': outcomes,
            'available_resources': available_resources[:5],  # Top 5 resources
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
