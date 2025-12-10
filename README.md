# NSW Science Learning Buddy

An intelligent multi-agent AI learning companion for the NSW Stage 4 Science curriculum (Years 7-8). This system provides personalised, conversational science education aligned with the NESA (NSW Education Standards Authority) syllabus.

## Overview

The NSW Science Learning Buddy uses advanced AI to create an engaging, adaptive learning experience for secondary students. Four specialised AI agents work together to deliver curriculum-aligned content, interactive lessons, quizzes, and emotional support.

### Key Features

- **Multi-Agent Architecture** - Four specialised AI agents coordinate to provide comprehensive learning support
- **NESA Curriculum Aligned** - 100% aligned with NSW Science 7-10 Syllabus (2023)
- **Conversational AI** - Natural, engaging conversations using Claude AI (Anthropic)
- **Free Textbook Integration** - OpenStax textbook recommendations with direct links
- **Interactive Quizzes** - Multiple choice and short answer assessments with instant feedback
- **Australian Context** - Examples and scenarios relevant to Australian students

## The Four Specialist Agents

| Agent | Persona | Role |
|-------|---------|------|
| **Curriculum Specialist** | - | Provides official NESA syllabus information, learning outcomes, and curriculum mapping |
| **Learning Specialist** | Nova | Delivers engaging, interactive lessons with videos, simulations, and activities |
| **Support Specialist** | Sage | Acts as a friendly learning buddy, offering encouragement and study tips |
| **Assessment Specialist** | - | Creates quizzes and provides detailed feedback on student responses |

## NSW Stage 4 Topics Covered

The system covers all 8 Stage 4 focus areas from the NESA syllabus:

1. **Observing the Universe** (SC4-OTU-01) - Solar system, stars, and astronomical technology
2. **Forces** (SC4-FRC-01) - Contact/non-contact forces, motion, and force diagrams
3. **Cells and Classification** (SC4-LW-02) - Cell structure, organelles, and taxonomy
4. **Solutions and Mixtures** (SC4-SOL-01) - Separation techniques and solubility
5. **Living Systems** (SC4-LW-01) - Ecosystems, body systems, and energy flow
6. **Periodic Table** (SC4-PRT-01) - Atoms, elements, and compounds
7. **Change** (SC4-CHG-01) - Physical and chemical changes
8. **Data Science** (SC4-DAT-01) - Scientific data analysis and interpretation

## Technology Stack

- **Backend**: Python 3.10 with Flask
- **AI Model**: Claude 3 Haiku (Anthropic) - Fast, cost-effective responses
- **Frontend**: HTML5, CSS3, JavaScript
- **Curriculum Data**: Official NESA DOCX documents parsed and indexed
- **Textbooks**: OpenStax free textbook catalog (CC BY 4.0)

## Getting Started

### Prerequisites

- Python 3.10+
- Anthropic API key (for Claude AI)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/nsw-science-agent.git
   cd nsw-science-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser to `http://localhost:5000`

### Using on Replit

1. Fork this Repl
2. Add your `ANTHROPIC_API_KEY` to Secrets
3. Click Run

## Project Structure

```
nsw-science-agent/
├── app.py                      # Flask application entry point
├── src/
│   ├── orchestrator.py         # Agent coordination and routing
│   ├── agents/
│   │   ├── claude_agent.py     # Base Claude AI integration
│   │   ├── curriculum_specialist.py
│   │   ├── learning_specialist.py
│   │   ├── support_specialist.py
│   │   └── assessment_specialist.py
│   ├── tools/
│   │   └── textbook_manager.py # OpenStax textbook recommendations
│   └── data/
│       ├── openstax_catalog.py # Textbook database
│       ├── nesa_curriculum.py  # Parsed NESA content
│       └── resource_catalog.py # Educational resources
├── static/
│   ├── css/style.css
│   └── js/app.js
├── templates/
│   └── index.html
└── attached_assets/
    └── nesa_docs/              # Official NESA documents
```

## Performance

The system has been tested against a comprehensive evaluation framework:

| Metric | Result |
|--------|--------|
| Average Response Time | 2.85 seconds |
| NESA Accuracy | 100% |
| Test Pass Rate | 15/15 (100%) |
| Australian Context | Present in all responses |

## Educational Resources

The system integrates with:

- **OpenStax Textbooks** - Free, peer-reviewed science textbooks (CC BY 4.0)
- **YouTube Videos** - Curated educational content
- **Interactive Simulations** - PhET and other science simulations
- **50+ Curated Resources** - Websites, videos, and activities

## License

This project is for educational purposes. 

- **OpenStax textbooks**: CC BY 4.0 License
- **NESA curriculum content**: Used under educational fair use

## Acknowledgements

- [NESA NSW](https://educationstandards.nsw.edu.au/) - NSW Science 7-10 Syllabus (2023)
- [OpenStax](https://openstax.org/) - Free, peer-reviewed textbooks
- [Anthropic](https://www.anthropic.com/) - Claude AI

## Documentation

- `COMPREHENSIVE_TESTING_RESULTS.md` - Full testing documentation
- `TESTING_COMPARISON_SUMMARY.md` - Performance comparison
- `replit.md` - Project architecture and history

---

**Built for NSW Science Education**
