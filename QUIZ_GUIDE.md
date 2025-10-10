# Interactive Quiz System Guide

## How the Quiz System Works

### 1. Taking a Quiz

**Step 1: Select Quiz Mode**
- Choose "Take a Quiz" from the dropdown menu
- Type a topic (e.g., "Energy", "Cells", "Forces")
- Click Send

**Step 2: Multiple Choice Questions (10 Questions)**
- Read each question carefully
- Select one answer (A, B, C, or D)
- Click "Check Answer" to see if you're correct
- Visual feedback:
  - ✅ **Green** = Correct answer
  - ❌ **Red** = Incorrect answer
- See explanation for each answer
- Repeat for all 10 questions

**Step 3: View Your Score**
- Click "Finish Multiple Choice Section"
- See your score:
  - Fraction format: X/10
  - Percentage: XX%
  - Encouraging message based on performance

**Step 4: Short Answer Questions (10 Questions)**
- Click "Continue to Short Answer Questions"
- Type your answer in the text box (2-4 sentences)
- Click "Show Expected Answer"
- Compare your answer with the expected answer
- Use for self-assessment (no automatic scoring)

### 2. Quiz Features

#### Multiple Choice
- **Answer Selection**: Must select before revealing answer
- **Automatic Scoring**: Tracks correct/incorrect answers
- **Visual Feedback**: Color-coded results
- **Explanations**: Learn why answers are correct/incorrect

#### Short Answer
- **Free Text Input**: Type your own response
- **Expected Answers**: See model answers
- **Self-Assessment**: Compare and evaluate your understanding
- **No Scoring**: Focus on learning, not grades

### 3. Score Interpretation

- **90-100%**: 🌟 Excellent! Strong understanding
- **70-89%**: 👍 Good job! Most concepts understood
- **50-69%**: 📚 Not bad! Review missed topics
- **Below 50%**: 💪 Keep practicing! Review and retry

### 4. Tips for Success

1. **Read Carefully**: Take time to understand each question
2. **Think Before Selecting**: Don't rush your answer
3. **Learn from Explanations**: Read why answers are correct
4. **Use Short Answers**: Write detailed responses for deeper learning
5. **Self-Assess**: Compare your answers honestly with expected answers
6. **Retry if Needed**: Practice makes perfect!

## Technical Details

### Quiz Data Format

**Multiple Choice:**
```
Q1. [Question text]
A) [Option 1]
B) [Option 2]
C) [Option 3]
D) [Option 4]
Answer: [Letter] - [Explanation]
```

**Short Answer:**
```
Q1. [Question text]
Expected Answer: [Model answer with key points]
```

### Architecture
- **Frontend**: `static/js/quiz.js` - Interactive quiz logic
- **Backend**: `src/agents/assessment_specialist.py` - Question generation
- **Styling**: `static/css/style.css` - Quiz UI components
- **Parser**: Regex-based question and answer extraction

### Future Enhancements
1. Format validation for malformed questions
2. Radio button locking after answer check
3. Progress tracking across sessions
4. Difficulty level selection
5. Topic-specific question banks
