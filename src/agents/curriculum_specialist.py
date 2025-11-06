from typing import Dict, Any, List
from src.agents.base_agent import BaseAgent
from src.config import NESA_CURRICULUM_UNITS, WORKING_SCIENTIFICALLY_SKILLS
from src.tools.resource_manager import load_resource_catalog, find_resources_by_unit, find_resources_by_query
from src.tools.utils import detect_outcomes
from src.data.nesa_official_content import get_nesa_teaching_content, get_key_ideas_for_topic, get_investigations_for_topic
from src.tools.textbook_manager import get_textbook_manager


class CurriculumSpecialist(BaseAgent):
    """Enhanced Curriculum Specialist with comprehensive NESA Stage 4 mapping"""
    
    # Comprehensive outcome mapping - Stage 4 (Years 7-8)
    OUTCOME_MAP = {
        # Forces and Motion
        "forces": {
            "content": ["SC4-FRC-01"],
            "ws": ["SC4-WS-02", "SC4-WS-05", "SC4-WS-06"],
            "topic": "Forces",
            "unit": "Physical World",
            "inquiry_questions": [
                "What are contact and non-contact forces?",
                "How do forces affect motion?",
                "How can we represent forces?"
            ]
        },
        "motion": {
            "content": ["SC4-FRC-01"],
            "ws": ["SC4-WS-02", "SC4-WS-05"],
            "topic": "Forces",
            "unit": "Physical World",
            "inquiry_questions": ["How do forces affect motion?", "What is the relationship between force and motion?"]
        },
        
        # Cells and Classification
        "cell": {
            "content": ["SC4-LW-02"],
            "ws": ["SC4-WS-01", "SC4-WS-04", "SC4-WS-08"],
            "topic": "Cells and Classification",
            "unit": "Living World",
            "inquiry_questions": [
                "What are cells and what are their features?",
                "How do we classify living things?",
                "What structural features are used for classification?"
            ]
        },
        "classification": {
            "content": ["SC4-LW-02"],
            "ws": ["SC4-WS-04", "SC4-WS-08"],
            "topic": "Cells and Classification",
            "unit": "Living World",
            "inquiry_questions": ["How do we classify living things?"]
        },
        
        # Living Systems
        "ecosystem": {
            "content": ["SC4-LW-01"],
            "ws": ["SC4-WS-01", "SC4-WS-06"],
            "topic": "Living Systems",
            "unit": "Living World",
            "inquiry_questions": [
                "How do living systems function?",
                "How do organisms interact and depend on each other?",
                "How do systems respond to change?"
            ]
        },
        "photosynthesis": {
            "content": ["SC4-LW-01"],
            "ws": ["SC4-WS-03", "SC4-WS-06"],
            "topic": "Living Systems",
            "unit": "Living World",
            "inquiry_questions": ["How do plants produce energy?", "What is the role of photosynthesis in ecosystems?"]
        },
        
        # Solutions and Mixtures
        "mixture": {
            "content": ["SC4-SOL-01"],
            "ws": ["SC4-WS-03", "SC4-WS-04", "SC4-WS-07"],
            "topic": "Solutions and Mixtures",
            "unit": "Chemical World",
            "inquiry_questions": [
                "What are mixtures and solutions?",
                "How can we separate mixtures?",
                "What properties enable separation?"
            ]
        },
        "solution": {
            "content": ["SC4-SOL-01"],
            "ws": ["SC4-WS-03", "SC4-WS-04"],
            "topic": "Solutions and Mixtures",
            "unit": "Chemical World",
            "inquiry_questions": ["What makes a solution?", "How does solubility work?"]
        },
        
        # Periodic Table and Atomic Structure
        "atom": {
            "content": ["SC4-PRT-01"],
            "ws": ["SC4-WS-01", "SC4-WS-08"],
            "topic": "Periodic Table and Atomic Structure",
            "unit": "Chemical World",
            "inquiry_questions": [
                "What are atoms, elements and compounds?",
                "How are elements organized?",
                "How do properties influence uses?"
            ]
        },
        "element": {
            "content": ["SC4-PRT-01"],
            "ws": ["SC4-WS-01", "SC4-WS-08"],
            "topic": "Periodic Table and Atomic Structure",
            "unit": "Chemical World",
            "inquiry_questions": ["What are elements?", "How is the periodic table organized?"]
        },
        "periodic": {
            "content": ["SC4-PRT-01"],
            "ws": ["SC4-WS-01", "SC4-WS-04"],
            "topic": "Periodic Table and Atomic Structure",
            "unit": "Chemical World",
            "inquiry_questions": ["How is the periodic table organized?"]
        },
        
        # Observing the Universe
        "space": {
            "content": ["SC4-OTU-01"],
            "ws": ["SC4-WS-01", "SC4-WS-04", "SC4-WS-06", "SC4-WS-08"],
            "topic": "Observing the Universe",
            "unit": "Earth and Space",
            "inquiry_questions": [
                "How do we observe our place in the Universe?",
                "How has technology enabled understanding?",
                "What patterns exist in the night sky?"
            ]
        },
        "universe": {
            "content": ["SC4-OTU-01"],
            "ws": ["SC4-WS-01", "SC4-WS-06"],
            "topic": "Observing the Universe",
            "unit": "Earth and Space",
            "inquiry_questions": ["How do we understand our place in the Universe?"]
        },
        "planet": {
            "content": ["SC4-OTU-01"],
            "ws": ["SC4-WS-01", "SC4-WS-04"],
            "topic": "Observing the Universe",
            "unit": "Earth and Space",
            "inquiry_questions": ["What is our Solar System?", "How do planets differ?"]
        },
        
        # Change
        "change": {
            "content": ["SC4-CHG-01"],
            "ws": ["SC4-WS-01", "SC4-WS-03", "SC4-WS-04"],
            "topic": "Change",
            "unit": "Chemical World",
            "inquiry_questions": [
                "What is the difference between physical and chemical changes?",
                "How can we identify chemical changes?",
                "What happens to atoms during changes?"
            ]
        },
        "chemical": {
            "content": ["SC4-CHG-01"],
            "ws": ["SC4-WS-03", "SC4-WS-04"],
            "topic": "Change",
            "unit": "Chemical World",
            "inquiry_questions": ["What are chemical changes?", "How do we identify chemical reactions?"]
        },
        
        # Data Science
        "data": {
            "content": ["SC4-DAT-01"],
            "ws": ["SC4-WS-03", "SC4-WS-07"],
            "topic": "Data Science 1",
            "unit": "Working Scientifically",
            "inquiry_questions": [
                "How do scientists collect data?",
                "How can we represent data?",
                "How do we analyze patterns and trends?"
            ]
        },
        "graph": {
            "content": ["SC4-DAT-01"],
            "ws": ["SC4-WS-03", "SC4-WS-07"],
            "topic": "Data Science 1",
            "unit": "Working Scientifically",
            "inquiry_questions": ["How do we represent data effectively?", "What graphs suit different data?"]
        }
    }
    
    # Common misconceptions database
    MISCONCEPTIONS = {
        "Forces": [
            "Confusing mass with weight",
            "Thinking objects need constant force to maintain motion",
            "Believing heavier objects fall faster in all conditions",
            "Misunderstanding balanced vs unbalanced forces"
        ],
        "Cells and Classification": [
            "Thinking all cells look the same",
            "Confusing cell wall with cell membrane",
            "Believing viruses are cells",
            "Assuming classification is just memorizing names"
        ],
        "Living Systems": [
            "Thinking photosynthesis only occurs in leaves",
            "Confusing respiration with breathing",
            "Believing all energy comes from the sun directly",
            "Misunderstanding food chains vs food webs"
        ],
        "Solutions and Mixtures": [
            "Confusing mixtures with compounds",
            "Thinking filtration removes all impurities",
            "Misunderstanding solubility vs dissolution",
            "Believing all mixtures are the same"
        ],
        "Periodic Table and Atomic Structure": [
            "Thinking atoms can be seen with regular microscopes",
            "Confusing atoms with molecules",
            "Believing elements and compounds are the same",
            "Misunderstanding atomic structure"
        ],
        "Observing the Universe": [
            "Confusing stars with planets",
            "Thinking the moon produces its own light",
            "Misunderstanding scale and distance in space",
            "Believing the Solar System is the entire Universe"
        ],
        "Change": [
            "Thinking all changes are reversible",
            "Confusing physical and chemical changes",
            "Believing mass is lost in chemical reactions",
            "Misunderstanding what happens to atoms during changes"
        ],
        "Data Science 1": [
            "Using inappropriate graph types",
            "Forgetting to label axes and units",
            "Confusing correlation with causation",
            "Ignoring anomalies in data"
        ]
    }
    
    def __init__(self):
        system_instruction = """You are the Enhanced Curriculum Specialist Agent for NSW Stage 4 Science (Years 7-8).
        
Your role is to provide comprehensive curriculum guidance including:
1. Map queries to specific NESA outcomes (content and Working Scientifically)
2. Provide clear learning objectives for the topic
3. Identify common misconceptions students face
4. Suggest differentiation strategies
5. Connect to relevant educational resources and free textbooks
6. Guide students toward inquiry-based learning

You have deep knowledge of all 8 Stage 4 focus areas and emphasize developing scientific thinking alongside content knowledge."""
        
        super().__init__("Curriculum Specialist", system_instruction)
        self.curriculum_data = NESA_CURRICULUM_UNITS
        self.student_progress = {}
        self.resource_catalog = load_resource_catalog()
        self.textbook_manager = get_textbook_manager()
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        student_query = request.get('query', '')
        student_id = request.get('student_id', 'default')
        
        # Enhanced topic detection
        matched_data = self._detect_topic(student_query.lower())
        
        # Get official NESA content for this topic
        nesa_content = get_nesa_teaching_content(matched_data["topic"])
        
        # Generate learning objectives
        learning_objectives = self._generate_learning_objectives(matched_data)
        
        # Get misconceptions
        misconceptions = self._get_misconceptions(matched_data["topic"])
        
        # Get official NESA key ideas and investigations
        key_ideas = nesa_content.get('key_ideas', [])
        investigations = nesa_content.get('investigations', [])
        background_knowledge = nesa_content.get('background_knowledge', [])
        
        # Find matching resources
        available_resources = find_resources_by_query(student_query, self.resource_catalog)
        
        # Get textbook recommendations
        textbook_recommendations = self.textbook_manager.search_textbooks(student_query)
        
        # Build enhanced response with official NESA content
        response_data = {
            'agent': self.agent_name,
            'topic': matched_data["topic"],
            'unit': matched_data["unit"],
            'content_outcomes': matched_data["content"],
            'ws_outcomes': matched_data["ws"],
            'inquiry_questions': matched_data.get("inquiry_questions", []),
            'learning_objectives': learning_objectives,
            'misconceptions': misconceptions,
            'key_ideas': key_ideas,
            'investigations': investigations,
            'background_knowledge': background_knowledge,
            'available_resources': available_resources[:5],
            'textbook_recommendations': textbook_recommendations,
            'next_action': 'route_to_learning_specialist'
        }
        
        # Generate human-readable summary
        prompt = f"""A Year 7-8 student asks: "{student_query}"

Topic: {matched_data['topic']}
NESA Outcomes: {', '.join(matched_data['content'])}
Working Scientifically: {', '.join(matched_data['ws'][:2])}

Learning Objectives:
{chr(10).join(f'• {obj}' for obj in learning_objectives)}

Common Misconceptions to Address:
{chr(10).join(f'• {misc}' for misc in misconceptions[:3])}

Provide a brief, friendly introduction (2-3 sentences) that:
1. Acknowledges the student's question
2. Explains what they'll learn about this topic
3. Connects to real-world relevance"""
        
        analysis = self.generate_response(prompt)
        response_data['analysis'] = analysis
        
        return response_data
    
    def _detect_topic(self, query: str) -> Dict[str, Any]:
        """Enhanced topic detection using keyword matching"""
        # Check each keyword in priority order
        for keyword, data in self.OUTCOME_MAP.items():
            if keyword in query:
                return data
        
        # Default to inquiry-based learning
        return {
            "content": ["SC4-WS-01"],
            "ws": ["SC4-WS-01", "SC4-WS-08"],
            "topic": "Scientific Inquiry",
            "unit": "Working Scientifically",
            "inquiry_questions": ["How do scientists investigate?", "What makes a good scientific question?"]
        }
    
    def _generate_learning_objectives(self, matched_data: Dict[str, Any]) -> List[str]:
        """Generate specific, measurable learning objectives"""
        topic = matched_data["topic"]
        
        objectives = [
            f"Explain key concepts of {topic} using scientific terminology",
            f"Apply {topic} knowledge to solve real-world problems",
            f"Conduct investigations related to {topic} using Working Scientifically skills",
            f"Communicate findings about {topic} using appropriate scientific formats"
        ]
        
        return objectives
    
    def _get_misconceptions(self, topic: str) -> List[str]:
        """Get common student misconceptions for the topic"""
        return self.MISCONCEPTIONS.get(topic, ["Check for understanding of basic scientific concepts"])
    
    def get_fallback_response(self, prompt: str) -> str:
        """Enhanced fallback with Stage 4 alignment"""
        return """Great question! This topic is part of the NSW Stage 4 Science curriculum. We'll explore the key scientific concepts, develop your investigation skills, and see how this connects to the real world. Let's start by understanding the fundamental principles and then apply them through hands-on inquiry."""
