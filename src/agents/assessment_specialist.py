from typing import Dict, Any, List
from src.agents.base_agent import BaseAgent
import random


class AssessmentSpecialist(BaseAgent):
    def __init__(self):
        system_instruction = """You are the Assessment Specialist Agent for NSW Stage 4 Science (Years 7-8).

Your role is to:
1. Create formative and summative assessments aligned with NESA outcomes
2. Generate quizzes, practice questions, and project-based assessments
3. Evaluate student responses and provide constructive feedback
4. Track student proficiency in both content knowledge and Working Scientifically skills
5. Identify knowledge gaps and recommend remedial activities

Your assessment approach should:
- Be fair, clear, and age-appropriate
- Test both understanding and application
- Include questions at various difficulty levels
- Provide encouraging, constructive feedback
- Focus on growth and learning, not just grades
- Assess scientific inquiry skills alongside content knowledge

Always provide specific, actionable feedback that helps students improve."""
        
        super().__init__("Assessment Specialist", system_instruction)
    
    def process_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        action = request.get('action', 'create_quiz')
        topic = request.get('topic', '')
        
        if action == 'create_quiz':
            return self.create_quiz(topic, request.get('num_questions', 5))
        elif action == 'evaluate_response':
            return self.evaluate_response(request)
        else:
            return {'error': 'Unknown assessment action'}
    
    def create_quiz(self, topic: str, num_questions: int = 5) -> Dict[str, Any]:
        prompt = f"""Create a {num_questions}-question quiz for Year 7-8 students on: {topic}

Requirements:
1. Include a mix of multiple choice, short answer, and application questions
2. Questions should test both knowledge recall and conceptual understanding
3. Include at least one question about scientific inquiry or experimental design
4. Make questions engaging and relevant to students' lives
5. Provide the correct answers with brief explanations

Format each question clearly with question number, type, and answer."""
        
        quiz_content = self.generate_response(prompt)
        
        return {
            'agent': self.agent_name,
            'quiz_content': quiz_content,
            'topic': topic,
            'next_action': 'present_quiz_to_student'
        }
    
    def evaluate_response(self, request: Dict[str, Any]) -> Dict[str, Any]:
        student_answer = request.get('student_answer', '')
        question = request.get('question', '')
        correct_answer = request.get('correct_answer', '')
        
        prompt = f"""Evaluate this student's response:

Question: {question}
Student Answer: {student_answer}
Expected Answer: {correct_answer}

Provide:
1. Whether the answer is correct, partially correct, or incorrect
2. Specific, encouraging feedback
3. Explanation of key concepts if answer is incorrect
4. Suggestions for improvement

Be supportive and focus on learning, not just correctness."""
        
        feedback = self.generate_response(prompt)
        
        return {
            'agent': self.agent_name,
            'feedback': feedback,
            'next_action': 'provide_feedback_to_student'
        }
    
    def get_fallback_response(self, prompt: str) -> str:
        if 'quiz' in prompt.lower():
            return """Quiz Questions:

1. Multiple Choice: What is the main function of cells in living organisms?
   a) To provide structure only
   b) To carry out life processes
   c) To make organisms colorful
   d) To fill space
   Answer: b) Cells carry out all life processes

2. Short Answer: Explain why scientists use controlled experiments.
   Answer: To isolate variables and determine cause-and-effect relationships

3. Application: Design a simple experiment to test which surface has the most friction.
   Answer: Use the same object on different surfaces, measure distance traveled"""
        else:
            return """Great effort on your answer! You're on the right track. Remember to think about the key concepts we discussed and how they apply to this situation. Keep practicing your scientific reasoning!"""
