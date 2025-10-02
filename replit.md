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
- Web-based student interface
- Integration with Google Vertex AI and Gemini
- Sample curriculum data for demonstration
- Interactive learning sessions

## Recent Changes
- Initial project setup (October 2, 2025)
- Multi-agent system architecture implemented
- Flask web interface created
- Google Vertex AI integration configured

## User Preferences
- System should act as a friendly learning buddy, not just content delivery
- Focus on developing scientific inquiry skills alongside content knowledge
- Provide personalized, adaptive learning pathways
- Connect science to real-world applications and careers
