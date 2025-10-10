class InteractiveQuiz {
    constructor(mcQuestions, saQuestions, topic) {
        this.mcQuestions = this.parseMCQuestions(mcQuestions);
        this.saQuestions = this.parseSAQuestions(saQuestions);
        this.topic = topic;
        this.mcAnswers = {};
        this.saAnswers = {};
        this.currentSection = 'mc';
    }

    parseMCQuestions(rawText) {
        const questions = [];
        const questionBlocks = rawText.split(/\n(?=Q\d+\.)/);
        
        questionBlocks.forEach(block => {
            const lines = block.trim().split('\n');
            if (lines.length < 2) return;
            
            const questionMatch = lines[0].match(/Q(\d+)\.\s*(.+)/);
            if (!questionMatch) return;
            
            const questionNum = questionMatch[1];
            const questionText = questionMatch[2];
            
            const options = [];
            let correctAnswer = '';
            let explanation = '';
            
            lines.slice(1).forEach(line => {
                const optionMatch = line.match(/^([A-D])\)\s*(.+)/);
                if (optionMatch) {
                    options.push({ letter: optionMatch[1], text: optionMatch[2] });
                }
                
                const answerMatch = line.match(/Answer:\s*([A-D])\s*-?\s*(.+)?/);
                if (answerMatch) {
                    correctAnswer = answerMatch[1];
                    explanation = answerMatch[2] || '';
                }
            });
            
            if (questionText && options.length > 0 && correctAnswer) {
                questions.push({
                    num: questionNum,
                    question: questionText,
                    options: options,
                    correctAnswer: correctAnswer,
                    explanation: explanation
                });
            }
        });
        
        return questions;
    }

    parseSAQuestions(rawText) {
        const questions = [];
        const questionBlocks = rawText.split(/\n(?=Q\d+\.)/);
        
        questionBlocks.forEach(block => {
            const lines = block.trim().split('\n');
            if (lines.length < 2) return;
            
            const questionMatch = lines[0].match(/Q(\d+)\.\s*(.+)/);
            if (!questionMatch) return;
            
            const questionNum = questionMatch[1];
            const questionText = questionMatch[2];
            
            let expectedAnswer = '';
            lines.slice(1).forEach(line => {
                if (line.includes('Expected Answer:')) {
                    expectedAnswer = line.replace('Expected Answer:', '').trim();
                }
            });
            
            if (questionText && expectedAnswer) {
                questions.push({
                    num: questionNum,
                    question: questionText,
                    expectedAnswer: expectedAnswer
                });
            }
        });
        
        return questions;
    }

    renderMCQuiz() {
        let html = `
            <div class="quiz-container">
                <div class="quiz-header">
                    <h3>📝 Multiple Choice Quiz: ${this.topic}</h3>
                    <p>Select your answer for each question. Click "Check Answer" to see if you're correct!</p>
                </div>
                <div class="quiz-questions">
        `;
        
        this.mcQuestions.forEach((q, index) => {
            html += `
                <div class="quiz-question" data-question="${index}">
                    <div class="question-text">
                        <strong>Question ${q.num}:</strong> ${q.question}
                    </div>
                    <div class="quiz-options">
                        ${q.options.map(opt => `
                            <div class="quiz-option" data-option="${opt.letter}">
                                <input type="radio" name="q${index}" id="q${index}_${opt.letter}" value="${opt.letter}">
                                <label for="q${index}_${opt.letter}">${opt.letter}) ${opt.text}</label>
                            </div>
                        `).join('')}
                    </div>
                    <button class="check-answer-btn" onclick="quizInstance.checkMCAnswer(${index})">Check Answer</button>
                    <div class="answer-feedback" id="feedback-${index}" style="display: none;"></div>
                </div>
            `;
        });
        
        html += `
                </div>
                <div class="quiz-footer">
                    <button class="finish-mc-btn" onclick="quizInstance.finishMCQuiz()">Finish Multiple Choice Section</button>
                </div>
            </div>
        `;
        
        return html;
    }

    renderSAQuiz() {
        let html = `
            <div class="quiz-container">
                <div class="quiz-header">
                    <h3>✍️ Short Answer Quiz: ${this.topic}</h3>
                    <p>Write your answers below. Click "Show Expected Answer" to see what's expected.</p>
                </div>
                <div class="quiz-questions">
        `;
        
        this.saQuestions.forEach((q, index) => {
            html += `
                <div class="quiz-question sa-question" data-question="${index}">
                    <div class="question-text">
                        <strong>Question ${q.num}:</strong> ${q.question}
                    </div>
                    <div class="sa-input-area">
                        <textarea id="sa-${index}" rows="4" placeholder="Type your answer here..."></textarea>
                    </div>
                    <button class="show-answer-btn" onclick="quizInstance.showSAAnswer(${index})">Show Expected Answer</button>
                    <div class="expected-answer" id="sa-feedback-${index}" style="display: none;"></div>
                </div>
            `;
        });
        
        html += `
                </div>
                <div class="quiz-footer">
                    <p class="sa-note">💡 Compare your answers with the expected answers to self-assess your understanding!</p>
                </div>
            </div>
        `;
        
        return html;
    }

    checkMCAnswer(questionIndex) {
        const question = this.mcQuestions[questionIndex];
        const selectedOption = document.querySelector(`input[name="q${questionIndex}"]:checked`);
        
        if (!selectedOption) {
            alert('Please select an answer first!');
            return;
        }
        
        const selectedAnswer = selectedOption.value;
        this.mcAnswers[questionIndex] = selectedAnswer;
        
        const feedbackDiv = document.getElementById(`feedback-${questionIndex}`);
        const isCorrect = selectedAnswer === question.correctAnswer;
        
        feedbackDiv.style.display = 'block';
        feedbackDiv.className = 'answer-feedback ' + (isCorrect ? 'correct' : 'incorrect');
        
        feedbackDiv.innerHTML = `
            <div class="feedback-content">
                ${isCorrect ? '✅ Correct!' : '❌ Incorrect'}
                <br>
                <strong>Correct Answer:</strong> ${question.correctAnswer}) ${question.options.find(o => o.letter === question.correctAnswer).text}
                ${question.explanation ? `<br><strong>Explanation:</strong> ${question.explanation}` : ''}
            </div>
        `;
        
        const questionDiv = document.querySelector(`[data-question="${questionIndex}"]`);
        questionDiv.querySelectorAll('.quiz-option').forEach(opt => {
            const letter = opt.dataset.option;
            if (letter === question.correctAnswer) {
                opt.classList.add('correct-option');
            } else if (letter === selectedAnswer && !isCorrect) {
                opt.classList.add('incorrect-option');
            }
        });
        
        const btn = questionDiv.querySelector('.check-answer-btn');
        btn.disabled = true;
        btn.textContent = 'Answered';
    }

    showSAAnswer(questionIndex) {
        const question = this.saQuestions[questionIndex];
        const textarea = document.getElementById(`sa-${questionIndex}`);
        const userAnswer = textarea.value.trim();
        
        this.saAnswers[questionIndex] = userAnswer;
        
        const feedbackDiv = document.getElementById(`sa-feedback-${questionIndex}`);
        feedbackDiv.style.display = 'block';
        feedbackDiv.className = 'expected-answer';
        
        feedbackDiv.innerHTML = `
            <div class="sa-feedback-content">
                <strong>Expected Answer:</strong>
                <p>${question.expectedAnswer}</p>
                ${userAnswer ? `<strong>Your Answer:</strong><p class="user-answer">${userAnswer}</p>` : ''}
            </div>
        `;
        
        const btn = document.querySelector(`[data-question="${questionIndex}"] .show-answer-btn`);
        btn.disabled = true;
        btn.textContent = 'Answer Revealed';
    }

    finishMCQuiz() {
        const totalQuestions = this.mcQuestions.length;
        const answeredCount = Object.keys(this.mcAnswers).length;
        
        if (answeredCount < totalQuestions) {
            if (!confirm(`You've only answered ${answeredCount} out of ${totalQuestions} questions. Continue anyway?`)) {
                return;
            }
        }
        
        let correctCount = 0;
        this.mcQuestions.forEach((q, index) => {
            if (this.mcAnswers[index] === q.correctAnswer) {
                correctCount++;
            }
        });
        
        const percentage = Math.round((correctCount / totalQuestions) * 100);
        
        const scoreHTML = `
            <div class="quiz-score">
                <h3>🎯 Multiple Choice Quiz Results</h3>
                <div class="score-display">
                    <div class="score-number">${correctCount}/${totalQuestions}</div>
                    <div class="score-percentage">${percentage}%</div>
                </div>
                <p class="score-message">${this.getScoreMessage(percentage)}</p>
                <button class="continue-btn" onclick="quizInstance.showSAQuiz()">Continue to Short Answer Questions →</button>
            </div>
        `;
        
        addMessage('Assessment Specialist', scoreHTML);
        
        const quizContainer = document.querySelector('.quiz-container');
        if (quizContainer) {
            quizContainer.style.display = 'none';
        }
    }

    getScoreMessage(percentage) {
        if (percentage >= 90) return '🌟 Excellent work! You have a strong understanding of this topic!';
        if (percentage >= 70) return '👍 Good job! You understand most of the key concepts.';
        if (percentage >= 50) return '📚 Not bad! Review the topics you missed and try again.';
        return '💪 Keep practicing! Review the material and don\'t give up!';
    }

    showSAQuiz() {
        const saHTML = this.renderSAQuiz();
        addMessage('Assessment Specialist', saHTML);
    }
}

let quizInstance = null;

function startInteractiveQuiz(mcQuestions, saQuestions, topic) {
    quizInstance = new InteractiveQuiz(mcQuestions, saQuestions, topic);
    const mcHTML = quizInstance.renderMCQuiz();
    addMessage('Assessment Specialist', mcHTML);
}
