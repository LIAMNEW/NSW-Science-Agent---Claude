# resource_catalog.py
# NSW Science Agent Learning System – Expanded Resource Catalog (with interactive simulations)
# NOTE: Keep the variable name `resources` — your indexer imports this.

resources = [
    # === Core references / syllabus ===
    {
        "ID": "nesa_syllabus_s4_v1",
        "Resource.URL": "https://storage.googleapis.com/bucketeducationagent/science-and-technology-k-6-syllabus-2017.pdf",
        "Resource.Title": "NESA Stage 4 Science Syllabus",
        "Resource.Type": "Syllabus",
        "Curriculum.Alignment": {
            "Unit": "All",
            "Outcomes": ["SC4-OUT-01", "SC4-FOR-01", "SC4-CLS-01", "SC4-SOL-01", "SC4-CHG-01", "SC4-WS-01", "SC4-WS-08"]
        },
        "Pedagogy.Learning_Objective": "Provide the overarching framework for Stage 4 Science learning in NSW.",
        "Pedagogy.Intended_Agent": "Curriculum Specialist",
        "Metadata.Difficulty_Level": "Advanced",
        "Metadata.Description": "Official NSW curriculum document outlining aims, outcomes, and content for Stage 4 Science.",
        "Metadata.Source": "NESA"
    },

    # === Existing media / OERs you had ===
    {
        "ID": "skilldog_habitats_y7",
        "Resource.URL": "https://www.youtube.com/watch?v=e1RLOulZm80",
        "Resource.Title": "Science with Skilldog - Year 7 Habitats",
        "Resource.Type": "YouTube Video",
        "Curriculum.Alignment": {"Unit": "Living World", "Outcomes": ["SC4-CLS-01"]},
        "Pedagogy.Learning_Objective": "Explain different types of habitats and the organisms that live in them.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Engaging overview of habitats and adaptations for Year 7.",
        "Metadata.Source": "YouTube (Science with Skilldog)"
    },
    {
        "ID": "csiro_separating_mixtures_oer",
        "Resource.URL": "https://storage.googleapis.com/bucketeducationagent/Separating-mixtures-resource%20(1).pdf",
        "Resource.Title": "CSIRO - Separating Mixtures Resource",
        "Resource.Type": "OER PDF/Webpage",
        "Curriculum.Alignment": {"Unit": "Chemical World", "Outcomes": ["SC4-SOL-01", "SC4-WS-03", "SC4-WS-04"]},
        "Pedagogy.Learning_Objective": "Learn different methods for separating mixtures.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Free educational resource explaining separation techniques with examples.",
        "Metadata.Source": "CSIRO"
    },
    {
        "ID": "nelson_biology_text",
        "Resource.URL": "https://storage.googleapis.com/bucketeducationagent/Nelson.pdf",
        "Resource.Title": "Nelson Biology Textbook Excerpt",
        "Resource.Type": "PDF Textbook",
        "Curriculum.Alignment": {"Unit": "Living World", "Outcomes": ["SC4-CLS-01", "SC4-BIO-01"]},
        "Pedagogy.Learning_Objective": "Provide foundational knowledge in biology relevant to Stage 4.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Textbook excerpt covering key concepts in living systems.",
        "Metadata.Source": "Nelson"
    },

    # === Your existing simulation (kept) ===
    {
        "ID": "phet_forces_distance_sim",
        "Resource.URL": "https://phet.colorado.edu/en/simulation/forces-and-motion-basics",
        "Resource.Title": "PhET – Forces and Motion Basics (Interactive)",
        "Resource.Type": "Interactive Simulation",
        "Curriculum.Alignment": {"Unit": "Physical World", "Outcomes": ["SC4-FOR-01", "SC4-WS-02"]},
        "Pedagogy.Learning_Objective": "Explore how forces act and change motion.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Interactive push/pull, friction, and motion exploration.",
        "Metadata.Source": "PhET Interactive Simulations"
    },

    # === Pearson (keep, but still a landing page — useful for theory/context) ===
    {
        "ID": "pearson_science_y8_ch4",
        "Resource.URL": "https://www.pearson.com/en-au/schools/secondary/science/pearson-science-new-south-wales-7-10/",
        "Resource.Title": "Pearson Science NSW – Year 8 Chapter 4 (Forces & Energy) – Sample/Info",
        "Resource.Type": "E-book Chapter (Info/Landing)",
        "Curriculum.Alignment": {"Unit": "Physical World", "Outcomes": ["SC4-FOR-01", "SC4-WS-05"]},
        "Pedagogy.Learning_Objective": "Explore how forces affect motion and simple machines.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Pearson NSW 7–10 series info page (useful for theory and teacher context).",
        "Metadata.Source": "Pearson Education Australia"
    },

    # === Fixed to point to a specific interactive page (Geoscience) ===
    {
        "ID": "geoscience_plate_tectonics",
        "Resource.URL": "https://www.ga.gov.au/education/classroom-resources/digital-interactives/plate-tectonics",
        "Resource.Title": "Geoscience Australia – Plate Tectonics (Interactive)",
        "Resource.Type": "Interactive Module",
        "Curriculum.Alignment": {"Unit": "Earth and Space", "Outcomes": ["SC4-CHG-01", "SC4-WS-03"]},
        "Pedagogy.Learning_Objective": "Understand plate boundaries, earthquakes, and continental drift.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Clickable, curriculum-aligned interactive for Australian context.",
        "Metadata.Source": "Geoscience Australia"
    },

    # === LabXchange – link to a specific virtual lab (fixed) ===
    {
        "ID": "labxchange_light_microscope",
        "Resource.URL": "https://www.labxchange.org/library/items/lb:LabXchange:90f3134d:html:1",
        "Resource.Title": "LabXchange – Using a Light Microscope (Virtual Lab)",
        "Resource.Type": "Interactive Lab",
        "Curriculum.Alignment": {"Unit": "Living World", "Outcomes": ["SC4-CLS-01", "SC4-WS-04"]},
        "Pedagogy.Learning_Objective": "Practise microscope use and observe cells safely and accurately.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Guided interactive lab with steps, safety, and observation tasks.",
        "Metadata.Source": "LabXchange"
    },

    # === Quick checks / quizzes you had (kept) ===
    {
        "ID": "hatzi_cells_quiz",
        "Resource.URL": "https://hatziscience.wordpress.com/living-world-stage-4/",
        "Resource.Title": "Hatzi Science – Cells and Habitats Quizzes",
        "Resource.Type": "Online Quiz",
        "Curriculum.Alignment": {"Unit": "Living World", "Outcomes": ["SC4-CLS-01", "SC4-WS-01"]},
        "Pedagogy.Learning_Objective": "Reinforce understanding of cell structure and classification.",
        "Pedagogy.Intended_Agent": "Assessment Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Quiz bank aligned to Stage 4 Living World concepts.",
        "Metadata.Source": "Hatzi Science"
    },
    {
        "ID": "studiosity_forces_quiz",
        "Resource.URL": "https://www.studiocity.com/student-resources/practice-tests/year-8-physical-science-forces-energy-quiz",
        "Resource.Title": "Studiocity – Year 8 Forces and Energy Quiz",
        "Resource.Type": "Online Quiz",
        "Curriculum.Alignment": {"Unit": "Physical World", "Outcomes": ["SC4-FOR-01", "SC4-WS-02"]},
        "Pedagogy.Learning_Objective": "Assess knowledge of forces, motion, and energy transfer.",
        "Pedagogy.Intended_Agent": "Assessment Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Short formative quiz covering key Physical World concepts.",
        "Metadata.Source": "Studiocity"
    },

    # === ACARA sample (kept) ===
    {
        "ID": "acara_year7_portfolio",
        "Resource.URL": "https://www.acara.edu.au/curriculum/work-samples/Year_7_Science_Portfolio_Above.pdf",
        "Resource.Title": "ACARA Work Sample – Year 7 Science Portfolio (Above Standard)",
        "Resource.Type": "Work Sample PDF",
        "Curriculum.Alignment": {"Unit": "All", "Outcomes": ["SC4-WS-01", "SC4-WS-02", "SC4-WS-08"]},
        "Pedagogy.Learning_Objective": "Model high-quality scientific recording and communication.",
        "Pedagogy.Intended_Agent": "Assessment Specialist",
        "Metadata.Difficulty_Level": "Advanced",
        "Metadata.Description": "Annotated work sample to help calibrate expectations.",
        "Metadata.Source": "ACARA"
    },

    # === Outreach / careers (kept) ===
    {
        "ID": "uow_stem_outreach",
        "Resource.URL": "https://www.uow.edu.au/science-medicine-health/schools-entities/outreach/",
        "Resource.Title": "UOW Science Outreach – School Programs",
        "Resource.Type": "Interactive Portal",
        "Curriculum.Alignment": {"Unit": "Science as a Human Endeavour", "Outcomes": ["SC4-WS-07", "SC4-WS-08"]},
        "Pedagogy.Learning_Objective": "Connect classroom science with real-world STEM pathways.",
        "Pedagogy.Intended_Agent": "Support Specialist",
        "Metadata.Difficulty_Level": "Extension",
        "Metadata.Description": "Workshops, demonstrations, and resources connecting schools with UOW.",
        "Metadata.Source": "University of Wollongong"
    },

    # === NEW: extra PhET / high-quality interactives to boost engagement ===
    {
        "ID": "phet_energy_skate_park",
        "Resource.URL": "https://phet.colorado.edu/en/simulation/energy-skate-park",
        "Resource.Title": "PhET – Energy Skate Park (Interactive)",
        "Resource.Type": "Interactive Simulation",
        "Curriculum.Alignment": {"Unit": "Physical World", "Outcomes": ["SC4-FOR-01", "SC4-WS-02"]},
        "Pedagogy.Learning_Objective": "Investigate kinetic/potential energy transformations and conservation.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Play with tracks, mass and friction to see energy changes.",
        "Metadata.Source": "PhET Interactive Simulations"
    },
    {
        "ID": "phet_states_of_matter",
        "Resource.URL": "https://phet.colorado.edu/en/simulation/states-of-matter-basics",
        "Resource.Title": "PhET – States of Matter: Basics (Interactive)",
        "Resource.Type": "Interactive Simulation",
        "Curriculum.Alignment": {"Unit": "Chemical World", "Outcomes": ["SC4-SOL-01", "SC4-WS-01"]},
        "Pedagogy.Learning_Objective": "Model particle motion in solids, liquids and gases.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Connect temperature, particle motion, and state changes.",
        "Metadata.Source": "PhET Interactive Simulations"
    },
    {
        "ID": "phet_density",
        "Resource.URL": "https://phet.colorado.edu/en/simulation/density",
        "Resource.Title": "PhET – Density (Interactive)",
        "Resource.Type": "Interactive Simulation",
        "Curriculum.Alignment": {"Unit": "Chemical World", "Outcomes": ["SC4-SOL-01", "SC4-WS-02"]},
        "Pedagogy.Learning_Objective": "Explore mass, volume and density relationships.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Predict floating/sinking using density reasoning.",
        "Metadata.Source": "PhET Interactive Simulations"
    },
    {
        "ID": "phet_circuit_kit_dc",
        "Resource.URL": "https://phet.colorado.edu/en/simulation/circuit-construction-kit-dc",
        "Resource.Title": "PhET – Circuit Construction Kit: DC (Interactive)",
        "Resource.Type": "Interactive Simulation",
        "Curriculum.Alignment": {"Unit": "Physical World", "Outcomes": ["SC4-PW2", "SC4-WS-02"]},
        "Pedagogy.Learning.Objective": "Build simple series/parallel circuits and measure current/voltage.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Drag-and-drop components with live meters and switches.",
        "Metadata.Source": "PhET Interactive Simulations"
    },
    {
        "ID": "phet_plate_tectonics",
        "Resource.URL": "https://phet.colorado.edu/en/simulation/plate-tectonics",
        "Resource.Title": "PhET – Plate Tectonics (Interactive)",
        "Resource.Type": "Interactive Simulation",
        "Curriculum.Alignment": {"Unit": "Earth and Space", "Outcomes": ["SC4-CHG-01", "SC4-WS-02"]},
        "Pedagogy.Learning_Objective": "Manipulate plate boundaries to explain mountains, trenches and volcanoes.",
        "Pedagogy.Intended_Agent": "Learning Specialist",
        "Metadata.Difficulty_Level": "Core",
        "Metadata.Description": "Model divergent, convergent and transform boundaries.",
        "Metadata.Source": "PhET Interactive Simulations"
    }
]
