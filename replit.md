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
**NSW Science 7-10 Syllabus (2023) - Stage 4 Focus Areas:**
1. **Observing the Universe** (SC4-OTU-01) - Patterns in sky, Solar System, technology in astronomy
2. **Forces** (SC4-FRC-01) - Contact and non-contact forces, motion, force diagrams
3. **Cells and Classification** (SC4-LW-02) - Cell structure, organelles, classification systems
4. **Solutions and Mixtures** (SC4-SOL-01) - Separation techniques, solubility, concentration
5. **Living Systems** (SC4-LW-01) - Energy flow, body systems, ecosystems
6. **Periodic Table and Atomic Structure** (SC4-PRT-01) - Atoms, elements, compounds
7. **Change** (SC4-CHG-01) - Physical and chemical changes, reversibility, conservation of mass
8. **Data Science 1** (SC4-DAT-01) - Scientific data analysis and interpretation

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
- **Authentic NESA curriculum content** from official documents
- NESA-recommended investigations, key ideas, and teaching strategies
- Comprehensive resource catalog (50+ educational resources)
- Interactive learning sessions with YouTube videos and simulations
- Enhanced quiz system (20 questions per topic)
- NESA outcome detection and resource matching

## Recent Changes
- **November 5, 2025 (Latest)**: Added Agent Selection for Individual Responses
  - **USER-REQUESTED**: Implemented agent selection dropdown to prevent multiple agents responding simultaneously
  - Added 4 clear options: Curriculum Info, Interactive Lesson (Nova), Learning Buddy Chat (Sage), Take a Quiz
  - Created separate orchestrator handlers for curriculum-only vs learning-only requests
  - Modified frontend to display only the selected agent's response
  - Eliminated overlap: Curriculum Info shows syllabus/outcomes only, Interactive Lesson shows teaching content only
  - Users now have full control over which AI specialist they interact with
  - All agents continue to use authentic NESA curriculum materials and Gemini AI for dynamic responses
  
- **November 5, 2025**: Fixed Robotic Agent Responses with Gemini Integration
  - **CRITICAL FIX**: Switched from unavailable Vertex AI to Google Gemini API (gemini-2.0-flash)
  - Created GeminiAgent base class for natural conversation capabilities
  - Redesigned Learning Specialist with "Nova" persona - enthusiastic, creative, engaging
  - Redesigned Support Specialist with "Sage" persona - empathetic, encouraging, varied
  - Implemented conversation memory with chat sessions for context-aware responses
  - Added explicit variation rules to prevent repetitive, robotic responses
  - Verified agents produce unique, conversational responses across multiple requests
  - Maintained all existing NESA curriculum integration and resource catalog features
  - Performance: Gemini responses take ~20-40s but deliver high-quality, personalized content
  
- **November 5, 2025**: Official NESA Curriculum Integration
  - **MAJOR UPGRADE**: System now uses 100% authentic NESA curriculum materials
  - Parsed 3 official NESA DOCX files (Syllabus Support, Full Syllabus, Sample Assessments)
  - Extracted official content for all 8 Stage 4 focus areas:
    * Key ideas (6-10 per topic)
    * NESA-recommended investigations (3-10 per topic)
    * Background knowledge requirements (3-8 per topic)
    * Teaching focus and depth study suggestions
  - Enhanced Curriculum Specialist to retrieve and display official NESA content
  - Updated Learning Specialist to use authentic NESA investigations in lesson generation
  - Added frontend display of key ideas, investigations, and background knowledge
  - All 8 topics verified: SC4-OTU-01, SC4-FRC-01, SC4-LW-02, SC4-SOL-01, SC4-LW-01, SC4-PRT-01, SC4-CHG-01, SC4-DAT-01
  - Replaced manually-created content with official curriculum materials
  
- **October 15, 2025**: Enhanced Curriculum Specialist Agent
  - Implemented comprehensive outcome mapping for all 8 Stage 4 focus areas
  - Added learning objectives generation for each topic
  - Included common misconceptions database to address student errors
  - Added inquiry questions aligned with NESA syllabus
  - Enhanced UI to display outcomes, objectives, and misconceptions
  - Improved topic detection with keyword matching
  - Added Working Scientifically outcomes for each topic
  
- **October 10, 2025**: Corrected to Stage 4 Syllabus
  - **CRITICAL FIX**: Updated from incorrect Stage 2 (K-6) to correct Stage 4 (Years 7-8) content
  - Implemented NSW Science 7-10 Syllabus (2023) with 8 focus areas
  - Updated all quiz questions to use actual Stage 4 outcomes (SC4-FRC-01, SC4-LW-02, SC4-PRT-01, SC4-SOL-01)
  - Created comprehensive Stage 4 fallback quizzes for all focus areas
  - Fixed syllabus alignment: system now targets secondary students (Years 7-8), not primary
  
- **October 10, 2025**: Interactive Quiz System
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
