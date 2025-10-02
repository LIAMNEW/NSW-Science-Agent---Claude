from typing import Dict, Any
from src.agents.curriculum_specialist import CurriculumSpecialist
from src.agents.learning_specialist import LearningSpecialist
from src.agents.assessment_specialist import AssessmentSpecialist
from src.agents.support_specialist import SupportSpecialist


class AgentOrchestrator:
    def __init__(self):
        print("Initializing Agent Orchestrator...")
        self.curriculum_agent = CurriculumSpecialist()
        self.learning_agent = LearningSpecialist()
        self.assessment_agent = AssessmentSpecialist()
        self.support_agent = SupportSpecialist()
        print("All agents initialized successfully!")
    
    def handle_student_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        query = request.get('query', '')
        request_type = request.get('type', 'learn')
        student_id = request.get('student_id', 'default')
        
        if request_type == 'learn':
            return self.handle_learning_request(query, student_id)
        elif request_type == 'quiz':
            return self.handle_assessment_request(query, student_id)
        elif request_type == 'help':
            return self.handle_support_request(query, student_id)
        else:
            return self.handle_learning_request(query, student_id)
    
    def handle_learning_request(self, query: str, student_id: str) -> Dict[str, Any]:
        curriculum_response = self.curriculum_agent.process_request({
            'query': query,
            'student_id': student_id
        })
        
        relevant_units = curriculum_response.get('relevant_units', [])
        curriculum_analysis = curriculum_response.get('analysis', '')
        
        learning_response = self.learning_agent.process_request({
            'topic': query,
            'curriculum_context': curriculum_analysis,
            'level': 'intermediate'
        })
        
        return {
            'type': 'learning',
            'curriculum_context': curriculum_analysis,
            'lesson': learning_response.get('lesson_content', ''),
            'resources': learning_response.get('resources', []),
            'units': relevant_units
        }
    
    def handle_assessment_request(self, topic: str, student_id: str) -> Dict[str, Any]:
        assessment_response = self.assessment_agent.process_request({
            'action': 'create_quiz',
            'topic': topic,
            'num_questions': 5
        })
        
        return {
            'type': 'assessment',
            'quiz': assessment_response.get('quiz_content', ''),
            'topic': topic
        }
    
    def handle_support_request(self, message: str, student_id: str, support_type: str = 'general') -> Dict[str, Any]:
        support_response = self.support_agent.process_request({
            'type': support_type,
            'message': message,
            'context': message
        })
        
        return {
            'type': 'support',
            'message': support_response.get('support_message') or support_response.get('response', ''),
            'agent': 'Support Specialist'
        }
