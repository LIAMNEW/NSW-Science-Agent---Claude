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
        
        if request_type == 'curriculum':
            return self.handle_curriculum_request(query, student_id)
        elif request_type == 'learn':
            return self.handle_learning_request(query, student_id)
        elif request_type == 'quiz':
            return self.handle_assessment_request(query, student_id)
        elif request_type == 'help':
            return self.handle_support_request(query, student_id)
        else:
            return self.handle_learning_request(query, student_id)
    
    def handle_curriculum_request(self, query: str, student_id: str) -> Dict[str, Any]:
        """Handle curriculum-only requests - just syllabus info, no lesson"""
        curriculum_response = self.curriculum_agent.process_request({
            'query': query,
            'student_id': student_id
        })
        
        return {
            'type': 'curriculum',
            'agent': 'Curriculum Specialist',
            'topic': curriculum_response.get('topic', query),
            'unit': curriculum_response.get('unit', ''),
            'content_outcomes': curriculum_response.get('content_outcomes', []),
            'ws_outcomes': curriculum_response.get('ws_outcomes', []),
            'inquiry_questions': curriculum_response.get('inquiry_questions', []),
            'learning_objectives': curriculum_response.get('learning_objectives', []),
            'misconceptions': curriculum_response.get('misconceptions', []),
            'key_ideas': curriculum_response.get('key_ideas', []),
            'investigations': curriculum_response.get('investigations', []),
            'background_knowledge': curriculum_response.get('background_knowledge', [])
        }
    
    def handle_learning_request(self, query: str, student_id: str) -> Dict[str, Any]:
        """Handle learning requests - just interactive lesson, no curriculum overhead"""
        # Get minimal curriculum context for the lesson
        curriculum_response = self.curriculum_agent.process_request({
            'query': query,
            'student_id': student_id
        })
        
        curriculum_analysis = curriculum_response.get('analysis', '')
        available_resources = curriculum_response.get('available_resources', [])
        
        learning_response = self.learning_agent.process_request({
            'topic': query,
            'curriculum_context': curriculum_analysis,
            'available_resources': available_resources,
            'level': 'intermediate'
        })
        
        return {
            'type': 'learning',
            'agent': 'Learning Specialist (Nova)',
            'topic': curriculum_response.get('topic', query),
            'lesson': learning_response.get('lesson_content', ''),
            'resources': learning_response.get('resources', []),
            'youtube_videos': learning_response.get('youtube_videos', []),
            'simulations': learning_response.get('simulations', [])
        }
    
    def handle_assessment_request(self, topic: str, student_id: str) -> Dict[str, Any]:
        assessment_response = self.assessment_agent.process_request({
            'action': 'create_quiz',
            'topic': topic,
            'num_questions': 10
        })
        
        return {
            'type': 'assessment',
            'multiple_choice': assessment_response.get('multiple_choice_questions', ''),
            'short_answer': assessment_response.get('short_answer_questions', ''),
            'quiz_summary': assessment_response.get('quiz_summary', ''),
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
