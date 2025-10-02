from flask import Flask, render_template, request, jsonify
from src.orchestrator import AgentOrchestrator
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

orchestrator = AgentOrchestrator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query', '')
    request_type = data.get('type', 'learn')
    
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    
    try:
        response = orchestrator.handle_student_request({
            'query': query,
            'type': request_type,
            'student_id': 'demo_student'
        })
        
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/assessment', methods=['POST'])
def handle_assessment():
    data = request.json
    topic = data.get('topic', '')
    
    try:
        response = orchestrator.handle_assessment_request(topic, 'demo_student')
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/support', methods=['POST'])
def handle_support():
    data = request.json
    message = data.get('message', '')
    support_type = data.get('support_type', 'general')
    
    try:
        response = orchestrator.handle_support_request(message, 'demo_student', support_type)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'agents': 'initialized'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
