# src/agents/curriculum_agent.py
"""
Enhanced Curriculum Agent - Maps queries to NESA Stage 4 outcomes
"""
from typing import Dict, Any, Optional, List


class CurriculumAgent:
    """
    Maps user intent to NESA Stage 4 Science outcomes.
    Acts as the 'source of truth' for curriculum alignment.
    """
    
    # Comprehensive outcome mapping based on NESA Stage 4 syllabus
    OUTCOME_MAP = {
        # Physical World
        "forces": {
            "content": ["SC4-FOR-01"],
            "ws": ["SC4-WS-02", "SC4-WS-05", "SC4-WS-06"],
            "topic": "Forces and Motion",
            "unit": "Physical World"
        },
        "motion": {
            "content": ["SC4-FOR-01"],
            "ws": ["SC4-WS-02", "SC4-WS-05"],
            "topic": "Forces and Motion",
            "unit": "Physical World"
        },
        "energy": {
            "content": ["SC4-FOR-01", "SC4-CHG-01"],
            "ws": ["SC4-WS-02", "SC4-WS-03"],
            "topic": "Energy Transfer and Transformation",
            "unit": "Physical World"
        },
        
        # Chemical World
        "mixture": {
            "content": ["SC4-SOL-01"],
            "ws": ["SC4-WS-03", "SC4-WS-04", "SC4-WS-07"],
            "topic": "Mixtures and Separation",
            "unit": "Chemical World"
        },
        "atom": {
            "content": ["SC4-SOL-01"],
            "ws": ["SC4-WS-01", "SC4-WS-08"],
            "topic": "Atoms and Elements",
            "unit": "Chemical World"
        },
        "matter": {
            "content": ["SC4-SOL-01"],
            "ws": ["SC4-WS-01", "SC4-WS-03"],
            "topic": "States of Matter",
            "unit": "Chemical World"
        },
        
        # Living World
        "cell": {
            "content": ["SC4-CLS-01"],
            "ws": ["SC4-WS-01", "SC4-WS-04", "SC4-WS-08"],
            "topic": "Cells and Classification",
            "unit": "Living World"
        },
        "ecosystem": {
            "content": ["SC4-CLS-01"],
            "ws": ["SC4-WS-01", "SC4-WS-06"],
            "topic": "Ecosystems and Habitats",
            "unit": "Living World"
        },
        "classification": {
            "content": ["SC4-CLS-01"],
            "ws": ["SC4-WS-04", "SC4-WS-08"],
            "topic": "Classification of Living Things",
            "unit": "Living World"
        },
        
        # Earth and Space
        "rock": {
            "content": ["SC4-CHG-01"],
            "ws": ["SC4-WS-01", "SC4-WS-03", "SC4-WS-04"],
            "topic": "Rock Cycle and Geological Change",
            "unit": "Earth and Space"
        },
        "space": {
            "content": ["SC4-OUT-01"],
            "ws": ["SC4-WS-01", "SC4-WS-04", "SC4-WS-06", "SC4-WS-08"],
            "topic": "Observing the Universe",
            "unit": "Earth and Space"
        },
        "plate": {
            "content": ["SC4-CHG-01"],
            "ws": ["SC4-WS-03", "SC4-WS-06"],
            "topic": "Plate Tectonics",
            "unit": "Earth and Space"
        }
    }

    def run(self, user_query: str, student_state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyze user query and map to NESA outcomes.
        
        Returns:
            Dict containing topic, outcomes, learning objectives, and misconceptions
        """
        q_lower = user_query.lower()
        
        # Find best match from outcome map
        matched_data = self._detect_topic(q_lower)
        
        # Get student-specific considerations
        reading_level = "Year 7"
        if student_state:
            reading_level = student_state.get("reading_level", "Year 7")
        
        # Build comprehensive outcome response
        return {
            "topic": matched_data["topic"],
            "unit": matched_data["unit"],
            "content_outcomes": matched_data["content"],
            "ws_outcomes": matched_data["ws"],
            "learning_objectives": self._generate_learning_objectives(matched_data),
            "misconceptions": self._get_common_misconceptions(matched_data["topic"]),
            "reading_level": reading_level,
            "differentiation_notes": self._get_differentiation_tips(reading_level)
        }
    
    def _detect_topic(self, query: str) -> Dict[str, Any]:
        """Match query keywords to curriculum topics"""
        # Check each keyword in priority order
        for keyword, data in self.OUTCOME_MAP.items():
            if keyword in query:
                return data
        
        # Default fallback to inquiry-based learning
        return {
            "content": ["SC4-WS-01"],
            "ws": ["SC4-WS-01", "SC4-WS-08"],
            "topic": "Scientific Inquiry",
            "unit": "Working Scientifically"
        }
    
    def _generate_learning_objectives(self, matched_data: Dict[str, Any]) -> List[str]:
        """Generate specific, measurable learning objectives"""
        topic = matched_data["topic"]
        
        objectives = [
            f"Explain key concepts of {topic} using scientific terminology",
            f"Apply {topic} knowledge to solve real-world problems",
            "Demonstrate Working Scientifically skills through practical investigation",
            "Communicate findings using appropriate scientific formats"
        ]
        
        return objectives
    
    def _get_common_misconceptions(self, topic: str) -> List[str]:
        """Return common student misconceptions for the topic"""
        misconception_db = {
            "Forces and Motion": [
                "Confusing mass with weight",
                "Thinking objects need constant force to maintain motion",
                "Believing heavier objects fall faster in all conditions"
            ],
            "Mixtures and Separation": [
                "Confusing mixtures with compounds",
                "Thinking filtration removes all impurities",
                "Misunderstanding solubility vs dissolution"
            ],
            "Cells and Classification": [
                "Thinking all cells look the same",
                "Confusing cell wall with cell membrane",
                "Believing viruses are cells"
            ],
            "Rock Cycle and Geological Change": [
                "Thinking rock formation happens quickly",
                "Confusing the three rock types",
                "Believing the rock cycle is linear"
            ],
            "Observing the Universe": [
                "Confusing stars with planets",
                "Thinking the moon produces its own light",
                "Misunderstanding scale and distance in space"
            ]
        }
        
        return misconception_db.get(topic, ["Check for understanding of basic concepts"])
    
    def _get_differentiation_tips(self, reading_level: str) -> str:
        """Provide differentiation guidance based on student level"""
        tips = {
            "Year 7": "Use concrete examples, visual aids, and scaffolded worksheets",
            "Year 8": "Increase abstract thinking, introduce data analysis, more independent inquiry",
            "Advanced": "Challenge with extension activities, research projects, cross-curricular links"
        }
        return tips.get(reading_level, tips["Year 7"])