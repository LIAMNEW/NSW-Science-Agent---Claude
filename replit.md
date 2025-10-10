# NSW Science Agentic Learning System

## Overview
An intelligent multi-agent AI learning companion for NSW Stage 4 Science curriculum (Years 7-8). The system uses Google Vertex AI to provide personalized, dynamic learning experiences through specialized AI agents.

## Project Architecture

### Multi-Agent System Components
1. **Agent Orchestrator (ADK Core)** - Central coordination system that routes student requests
2. **Curriculum Specialist Agent** - Maintains NESA syllabus knowledge and tracks student progress
3. **Learning Specialist Agent** - Generates lesson plans and delivers learning content
4. **Assessment Specialist Agent** - Creates quizzes and provides feedback
5. **Support Specialist Agent** - Acts as learning buddy/tutor with emotional support

### Technology Stack
- **Backend**: Python with Flask
- **AI Framework**: Google Vertex AI with Gemini 2.5
- **Agent Framework**: ADK (Agent Development Kit) and A2A (Agent-to-Agent) protocol
- **Tools**: MCP (Model Context Protocol) for external resource connections

### NESA Curriculum Coverage
**Content Strands:**
- Working Scientifically (inquiry, investigation, data analysis skills)
- Physical World (Forces, energy, motion)
- Chemical World (States of matter, atoms, elements)
- Earth and Space (Earth's systems, astronomy)
- Living World (Cells, ecosystems, human body systems)

**Working Scientifically Skills:**
- Questioning and predicting
- Planning and conducting investigations
- Processing and analyzing data
- Communicating scientific ideas

## Project Status
Current implementation provides:
- Multi-agent architecture with orchestrator
- Web-based student interface with purple gradient UI
- Integration with Google Vertex AI and Gemini
- Comprehensive resource catalog (50+ educational resources)
- Interactive learning sessions with YouTube videos and simulations
- Enhanced quiz system (20 questions per topic)
- NESA outcome detection and resource matching

## Recent Changes
- **October 10, 2025 (Latest)**: Interactive Quiz System
  - Built interactive quiz interface with answer selection before reveal
  - Added automatic scoring for multiple choice questions (shows X/10 and percentage)
  - Implemented expected answer display for short answer (no scoring, self-assessment)
  - Visual feedback: green for correct, red for incorrect answers
  - Complete quiz flow: MC quiz → Score → SA quiz
  
- **October 10, 2025**: Enhanced resource integration
  - Integrated comprehensive resource catalog (50+ resources)
  - Added YouTube video embedding and interactive simulations
  - Enhanced quiz system: 10 multiple choice + 10 short answer questions
  - Upgraded Curriculum Specialist with outcome detection
  - Upgraded Learning Specialist with Gemini-powered explanations
  - Added resource categorization and URL access
  
- **October 2, 2025**: Initial project setup
  - Multi-agent system architecture implemented
  - Flask web interface created
  - Google Vertex AI integration configured

## User Preferences
- System should act as a friendly learning buddy, not just content delivery
- Focus on developing scientific inquiry skills alongside content knowledge
- Provide personalized, adaptive learning pathways
- Connect science to real-world applications and careers
