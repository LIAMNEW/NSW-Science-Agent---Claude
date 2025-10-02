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
        if (data.curriculum_context) {
            addMessage('Curriculum Specialist', data.curriculum_context);
        }
        
        if (data.lesson) {
            addMessage('Learning Specialist', data.lesson);
        }
        
        if (data.resources && data.resources.length > 0) {
            let resourcesHtml = '<strong>Recommended Resources:</strong><br>';
            data.resources.forEach(resource => {
                resourcesHtml += `<div class="resource-item">
                    <strong>${resource.title}</strong><br>
                    Type: ${resource.type} | Source: ${resource.source}
                </div>`;
            });
            addMessage('Learning Specialist', resourcesHtml);
        }
        
        if (data.units && data.units.length > 0) {
            let unitsHtml = '<strong>Relevant NESA Curriculum Units:</strong><br>';
            data.units.forEach(unit => {
                unitsHtml += `<div class="curriculum-unit">
                    <strong>${unit.unit}</strong> (${unit.code})<br>
                    Topics: ${unit.topics.join(', ')}
                </div>`;
            });
            addMessage('Curriculum Specialist', unitsHtml);
        }
    } else if (queryType === 'quiz') {
        if (data.quiz) {
            addMessage('Assessment Specialist', data.quiz);
        }
    } else if (queryType === 'help') {
        if (data.message) {
            addMessage('Support Specialist', data.message);
        }
    }
}

document.getElementById('queryInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendQuery();
    }
});
