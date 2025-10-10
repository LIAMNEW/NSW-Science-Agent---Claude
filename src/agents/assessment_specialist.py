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
        # Generate 10 multiple choice questions
        mc_prompt = f"""Create 10 multiple choice questions for Year 7-8 students on: {topic}

Requirements for EACH question:
1. Test different aspects of {topic} (concepts, applications, experiments, real-world connections)
2. Include 4 options (A, B, C, D) with only ONE correct answer
3. Make distractors plausible but clearly incorrect
4. Vary difficulty from basic recall to higher-order thinking
5. Relate to NSW Stage 4 Science curriculum outcomes

Format:
Q1. [Question text]
A) [Option]
B) [Option]
C) [Option]
D) [Option]
Answer: [Letter] - [Brief explanation]

Provide all 10 questions."""
        
        mc_questions = self.generate_response(mc_prompt)
        
        # Generate 10 short answer questions
        sa_prompt = f"""Create 10 short answer questions for Year 7-8 students on: {topic}

Requirements for EACH question:
1. Require 2-4 sentence responses
2. Test understanding, not just recall
3. Include: definitions, explanations, comparisons, applications, and scientific inquiry
4. Vary difficulty levels
5. Align with NSW Working Scientifically skills

Format:
Q1. [Question requiring short written response]
Expected Answer: [Key points for full credit]

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
        if 'Create 10 multiple choice' in prompt:
            # Extract topic from prompt
            import re
            topic_match = re.search(r'on: (.+?)\n', prompt)
            topic = topic_match.group(1) if topic_match else "this topic"
            
            return f"""Q1. What is the primary characteristic of {topic}?
A) It only occurs in laboratories
B) It involves observable phenomena and measurable properties
C) It requires expensive equipment
D) It only applies to living things
Answer: B - Science involves studying observable, measurable phenomena

Q2. In {topic}, which scientific method is most commonly used?
A) Guessing randomly
B) Asking opinions
C) Systematic observation and experimentation
D) Reading social media
Answer: C - Scientific method requires systematic investigation

Q3. How does {topic} relate to everyday life?
A) It has no practical applications
B) It explains natural phenomena we observe daily
C) It only matters to scientists
D) It's purely theoretical
Answer: B - Science concepts explain real-world observations

Q4. What Working Scientifically skill is essential when studying {topic}?
A) Memorization only
B) Data collection and analysis
C) Speed reading
D) Artistic ability
Answer: B - Scientific inquiry requires collecting and analyzing data

Q5. Which tool might scientists use to investigate {topic}?
A) Only calculators
B) Appropriate measuring instruments and observations
C) Crystal balls
D) Random guessing
Answer: B - Scientists use proper tools for measurement

Q6. What is a key safety consideration when exploring {topic}?
A) Safety is not important
B) Following proper procedures and using equipment correctly
C) Working alone always
D) Ignoring instructions
Answer: B - Safety protocols are essential in science

Q7. How can you test your understanding of {topic}?
A) Never practice
B) Conduct experiments and solve problems
C) Just read once
D) Avoid questions
Answer: B - Active practice builds understanding

Q8. What makes {topic} important in NSW Stage 4 Science?
A) It's not important
B) It builds foundational knowledge for future learning
C) It's just for tests
D) It has no connection to curriculum
Answer: B - Foundational concepts support ongoing learning

Q9. Which statement about {topic} is most accurate?
A) It never changes
B) Our understanding evolves through research and discovery
C) One person knows everything
D) Questions are discouraged
Answer: B - Science knowledge grows through investigation

Q10. What's the best approach to learning {topic}?
A) Passive listening only
B) Active engagement with questions, experiments, and practice
C) Avoiding difficult concepts
D) Memorizing without understanding
Answer: B - Active learning promotes deep understanding"""
        elif 'Create 10 short answer' in prompt:
            import re
            topic_match = re.search(r'on: (.+?)\n', prompt)
            topic = topic_match.group(1) if topic_match else "this topic"
            
            return f"""Q1. Explain the main concept of {topic} in your own words.
Expected Answer: Should include definition, key characteristics, and basic explanation of how it works or why it's important.

Q2. Describe a real-world example where {topic} is observed or applied.
Expected Answer: Specific example from daily life, explanation of the connection, and why it demonstrates the concept.

Q3. How would you design an experiment to investigate {topic}?
Expected Answer: Clear hypothesis, variables to test, method of data collection, and expected observations.

Q4. Compare and contrast two aspects of {topic}.
Expected Answer: Identification of similarities, key differences, and explanation of significance.

Q5. What Working Scientifically skills are important when studying {topic}? Explain why.
Expected Answer: Mention of relevant WS skills (observation, data analysis, etc.), justification for each, application to the topic.

Q6. Explain how {topic} connects to other areas of science.
Expected Answer: Identification of related concepts, explanation of connections, integrated understanding.

Q7. What questions do scientists still have about {topic}?
Expected Answer: Identification of unknowns, importance of continued research, examples of current investigations.

Q8. How has our understanding of {topic} changed over time?
Expected Answer: Historical perspective, key discoveries, evolution of knowledge, modern understanding.

Q9. Describe the role of {topic} in the NSW science curriculum.
Expected Answer: Curriculum relevance, learning outcomes addressed, connection to Stage 4 goals.

Q10. What safety considerations or ethical issues relate to {topic}?
Expected Answer: Specific safety protocols or ethical concerns, importance of responsible practice, real-world implications."""
        else:
            return """Great effort on your answer! You're on the right track. Remember to think about the key concepts we discussed and how they apply to this situation. Keep practicing your scientific reasoning!"""
