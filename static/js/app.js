function addMessage(sender, content, isStudent = false) {
    const messagesDiv = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isStudent ? 'student-message' : 'agent-message'}`;
    
    const senderName = isStudent ? 'You' : sender;
    messageDiv.innerHTML = `<strong>${senderName}:</strong><div>${formatContent(content)}</div>`;
    
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function formatContent(content) {
    if (typeof content === 'object') {
        return `<pre>${JSON.stringify(content, null, 2)}</pre>`;
    }
    
    content = content.replace(/\n/g, '<br>');
    
    content = content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    content = content.replace(/\*(.*?)\*/g, '<em>$1</em>');
    
    return content;
}

function selectTopic(topic) {
    document.getElementById('queryInput').value = topic;
    document.getElementById('queryType').value = 'learn';
}

async function sendQuery() {
    const input = document.getElementById('queryInput');
    const queryType = document.getElementById('queryType').value;
    const query = input.value.trim();
    
    if (!query) {
        alert('Please enter a question or topic!');
        return;
    }
    
    addMessage('You', query, true);
    input.value = '';
    
    const sendBtn = document.getElementById('sendBtn');
    sendBtn.disabled = true;
    sendBtn.innerHTML = 'Thinking<span class="loading"></span>';
    
    try {
        const response = await fetch('/api/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                query: query,
                type: queryType
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            addMessage('System', `Error: ${data.error}`);
        } else {
            handleResponse(data, queryType);
        }
    } catch (error) {
        addMessage('System', `Error: ${error.message}`);
    } finally {
        sendBtn.disabled = false;
        sendBtn.innerHTML = 'Send';
    }
}

function handleResponse(data, queryType) {
    if (queryType === 'learn') {
        // Display enhanced curriculum information
        if (data.topic || data.content_outcomes) {
            let curriculumHtml = '<div class="curriculum-info">';
            
            if (data.topic) {
                curriculumHtml += `<strong>📚 Topic:</strong> ${data.topic}<br>`;
                if (data.unit) {
                    curriculumHtml += `<strong>Unit:</strong> ${data.unit}<br>`;
                }
            }
            
            if (data.content_outcomes && data.content_outcomes.length > 0) {
                curriculumHtml += `<br><strong>🎯 NESA Outcomes:</strong><br>`;
                data.content_outcomes.forEach(outcome => {
                    curriculumHtml += `<span class="outcome-badge">${outcome}</span><br>`;
                });
            }
            
            if (data.inquiry_questions && data.inquiry_questions.length > 0) {
                curriculumHtml += `<br><strong>❓ Key Questions:</strong><br>`;
                data.inquiry_questions.forEach(q => {
                    curriculumHtml += `• ${q}<br>`;
                });
            }
            
            if (data.learning_objectives && data.learning_objectives.length > 0) {
                curriculumHtml += `<br><strong>✓ Learning Objectives:</strong><br>`;
                data.learning_objectives.forEach(obj => {
                    curriculumHtml += `• ${obj}<br>`;
                });
            }
            
            if (data.misconceptions && data.misconceptions.length > 0) {
                curriculumHtml += `<br><strong>⚠️ Common Misconceptions to Avoid:</strong><br>`;
                data.misconceptions.forEach(misc => {
                    curriculumHtml += `• ${misc}<br>`;
                });
            }
            
            if (data.key_ideas && data.key_ideas.length > 0) {
                curriculumHtml += `<br><strong>💡 NESA Key Ideas:</strong><br>`;
                data.key_ideas.forEach(idea => {
                    curriculumHtml += `• ${idea}<br>`;
                });
            }
            
            if (data.background_knowledge && data.background_knowledge.length > 0) {
                curriculumHtml += `<br><strong>📖 Background Knowledge:</strong><br>`;
                data.background_knowledge.forEach(bg => {
                    curriculumHtml += `• ${bg}<br>`;
                });
            }
            
            if (data.investigations && data.investigations.length > 0) {
                curriculumHtml += `<br><strong>🔬 NESA-Recommended Investigations:</strong><br>`;
                data.investigations.slice(0, 3).forEach(inv => {
                    curriculumHtml += `<div class="investigation-item">• ${inv}</div>`;
                });
                if (data.investigations.length > 3) {
                    curriculumHtml += `<em>...and ${data.investigations.length - 3} more investigations</em><br>`;
                }
            }
            
            curriculumHtml += '</div>';
            addMessage('Curriculum Specialist', curriculumHtml);
        }
        
        // Note: curriculum_context removed to avoid duplicate display
        // The enhanced curriculum info above already provides all necessary details
        
        if (data.lesson) {
            addMessage('Learning Specialist', data.lesson);
        }
        
        // Display YouTube videos
        if (data.youtube_videos && data.youtube_videos.length > 0) {
            let videosHtml = '<strong>📺 YouTube Learning Videos:</strong><br>';
            data.youtube_videos.forEach(video => {
                const videoId = extractYouTubeId(video.url);
                if (videoId) {
                    videosHtml += `<div class="resource-item video-item">
                        <strong>${video.title}</strong><br>
                        <a href="${video.url}" target="_blank" class="resource-link">Watch on YouTube →</a><br>
                        <div class="video-embed">
                            <iframe width="100%" height="200" src="https://www.youtube.com/embed/${videoId}" 
                                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                allowfullscreen></iframe>
                        </div>
                    </div>`;
                } else {
                    videosHtml += `<div class="resource-item">
                        <strong>${video.title}</strong><br>
                        <a href="${video.url}" target="_blank" class="resource-link">Watch Video →</a>
                    </div>`;
                }
            });
            addMessage('Learning Specialist', videosHtml);
        }
        
        // Display interactive simulations
        if (data.simulations && data.simulations.length > 0) {
            let simsHtml = '<strong>🔬 Interactive Simulations:</strong><br>';
            data.simulations.forEach(sim => {
                simsHtml += `<div class="resource-item simulation-item">
                    <strong>${sim.title}</strong><br>
                    <p>${sim.description || 'Interactive learning experience'}</p>
                    <a href="${sim.url}" target="_blank" class="resource-link">Launch Simulation →</a>
                </div>`;
            });
            addMessage('Learning Specialist', simsHtml);
        }
        
        // Display other resources
        if (data.resources && data.resources.length > 0) {
            let resourcesHtml = '<strong>📚 Additional Resources:</strong><br>';
            data.resources.forEach(resource => {
                resourcesHtml += `<div class="resource-item">
                    <strong>${resource.title}</strong><br>
                    Type: ${resource.type} | Source: ${resource.source}<br>
                    ${resource.url ? `<a href="${resource.url}" target="_blank" class="resource-link">Access Resource →</a>` : ''}
                </div>`;
            });
            addMessage('Learning Specialist', resourcesHtml);
        }
    } else if (queryType === 'quiz') {
        if (data.quiz_summary) {
            addMessage('Assessment Specialist', data.quiz_summary);
        }
        
        // Start interactive quiz
        if (data.multiple_choice && data.short_answer) {
            startInteractiveQuiz(data.multiple_choice, data.short_answer, data.topic);
        }
    } else if (queryType === 'help') {
        if (data.message) {
            addMessage('Support Specialist', data.message);
        }
    }
}

function extractYouTubeId(url) {
    if (!url) return null;
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
}

document.getElementById('queryInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendQuery();
    }
});
