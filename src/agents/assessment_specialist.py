from typing import Dict, Any, List
from src.agents.base_agent import BaseAgent
from src.data.syllabus_content import get_topic_content, STAGE_4_WS_SKILLS
from src.data.stage4_fallback_quizzes import get_mc_fallback
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
        # Get syllabus content for this topic
        syllabus_content = get_topic_content(topic)
        
        # Extract key information
        outcomes = syllabus_content.get('outcomes', [])
        inquiry_questions = syllabus_content.get('inquiry_questions', [])
        key_concepts = syllabus_content.get('key_concepts', {})
        
        # Build detailed concept list
        concept_details = []
        for concept_name, details in key_concepts.items():
            concept_details.append(f"{concept_name}: {', '.join(details[:3])}")
        
        # Generate 10 multiple choice questions based on syllabus
        mc_prompt = f"""Create 10 multiple choice questions for NSW Stage 4 (Years 7-8) students on: {topic}

SYLLABUS OUTCOMES:
{chr(10).join(outcomes)}

INQUIRY QUESTIONS:
{chr(10).join(inquiry_questions)}

KEY CONCEPTS TO COVER:
{chr(10).join(concept_details)}

WORKING SCIENTIFICALLY SKILLS:
{chr(10).join(STAGE_4_WS_SKILLS['Planning and conducting investigations'][:3])}

Requirements for EACH question:
1. Base questions on the ACTUAL syllabus content above
2. Use inquiry questions as inspiration for higher-order questions
3. Include 4 options (A, B, C, D) with only ONE correct answer
4. Make distractors plausible but clearly incorrect
5. Cover different key concepts from the syllabus
6. Include at least 2 questions on Working Scientifically skills
7. Make questions relevant to Years 7-8 understanding level

Format:
Q1. [Question text based on syllabus concepts]
A) [Option]
B) [Option]
C) [Option]
D) [Option]
Answer: [Letter] - [Brief explanation referencing syllabus]

Provide all 10 questions."""
        
        mc_questions = self.generate_response(mc_prompt)
        
        # Generate 10 short answer questions based on syllabus
        sa_prompt = f"""Create 10 short answer questions for NSW Stage 4 (Years 7-8) students on: {topic}

SYLLABUS OUTCOMES:
{chr(10).join(outcomes)}

INQUIRY QUESTIONS:
{chr(10).join(inquiry_questions)}

KEY CONCEPTS TO ASSESS:
{chr(10).join(concept_details)}

Requirements for EACH question:
1. Base questions on ACTUAL inquiry questions and key concepts from syllabus
2. Require 3-5 sentence responses appropriate for Years 7-8
3. Test understanding, not just recall
4. Include: explanations of syllabus concepts, real-world examples, investigations
5. Focus on Working Scientifically skills: questioning, planning investigations, analyzing data
6. Questions should help students demonstrate syllabus outcomes

Format:
Q1. [Question from syllabus inquiry questions or key concepts]
Expected Answer: [Key syllabus points - specific concepts, examples, and Working Scientifically skills]

Provide all 10 questions."""
        
        sa_questions = self.generate_response(sa_prompt)
        
        return {
            'agent': self.agent_name,
            'multiple_choice_questions': mc_questions,
            'short_answer_questions': sa_questions,
            'quiz_summary': f"20 total questions generated for {topic}:\n- 10 Multiple Choice\n- 10 Short Answer",
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
        """Fallback responses using Stage 4 content when Vertex AI unavailable"""
        if 'Create 10 multiple choice' in prompt:
            # Extract topic from prompt
            import re
            topic_match = re.search(r'on: (.+?)\n', prompt)
            topic = topic_match.group(1) if topic_match else "this topic"
            
            # Use Stage 4 fallback quizzes (covers all 8 focus areas)
            return get_mc_fallback(topic.lower())
        
        elif 'Create 10 short answer' in prompt:
            # Extract topic
            import re
            topic_match = re.search(r'on: (.+?)\n', prompt)
            topic = topic_match.group(1) if topic_match else "this topic"
            
            # Get syllabus content for Stage 4
            syllabus_content = get_topic_content(topic)
            inquiry_questions = syllabus_content.get('inquiry_questions', [])
            first_inquiry = inquiry_questions[0] if inquiry_questions else f"Explain the main concepts of {topic}."
            
            # Generic Stage 4 short answer template
            return f"""Q1. {first_inquiry}
Expected Answer: Provide a detailed explanation covering the main concepts, key scientific principles, and real-world applications relevant to Stage 4 (Years 7-8) understanding.

Q2. Describe how you would investigate {topic} scientifically.
Expected Answer: State a testable question, identify variables, describe method, explain how to collect and record data, mention safety considerations relevant to Years 7-8.

Q3. How does {topic} relate to everyday life and real-world applications?
Expected Answer: Give specific examples from daily life, technology, or industry. Explain the scientific principles involved.

Q4. What Working Scientifically skills are important when studying {topic}?
Expected Answer: Discuss questioning, planning investigations, conducting experiments, analyzing data, and communicating findings as they apply to this topic.

Q5. Explain the key scientific concepts underlying {topic}.
Expected Answer: Define important terms, explain relationships between concepts, use scientific vocabulary appropriate for Years 7-8.

Q6. Compare and contrast different aspects of {topic}.
Expected Answer: Identify similarities and differences, explain significance, demonstrate understanding of Stage 4 concepts.

Q7. How has our understanding of {topic} evolved through scientific discoveries?
Expected Answer: Describe how observations and evidence have shaped our knowledge, mention key discoveries or technologies.

Q8. Design an investigation to test a hypothesis about {topic}.
Expected Answer: State hypothesis, identify independent/dependent variables, describe controlled conditions, explain data collection method.

Q9. What connections exist between {topic} and other areas of science?
Expected Answer: Identify related concepts in physics, chemistry, biology, or Earth science. Explain how they connect.

Q10. Analyze data or observations related to {topic} and draw conclusions.
Expected Answer: Interpret given information, identify patterns or trends, make evidence-based conclusions, suggest further investigations."""
        
        else:
            return """Great effort on your answer! You're demonstrating good scientific thinking. Consider how this connects to the NSW Stage 4 outcomes we've been studying. Keep developing your inquiry and investigation skills!"""
