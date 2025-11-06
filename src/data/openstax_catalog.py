"""
OpenStax Textbook Catalog for NSW Stage 4 Science
Maps free, open-source science textbooks to NSW curriculum topics
"""

OPENSTAX_TEXTBOOKS = {
    "biology_2e": {
        "title": "Biology 2e",
        "url": "https://openstax.org/details/books/biology-2e",
        "pdf_url": "https://openstax.org/books/biology-2e/pages/1-introduction",
        "cover_url": "https://d3bxy9euw4e147.cloudfront.net/oscms-prodcms/media/documents/biology_2e_book_card.svg",
        "subjects": ["Biology", "Life Science"],
        "grade_level": "High School / College",
        "license": "CC BY 4.0",
        "description": "Comprehensive biology textbook covering cells, genetics, evolution, ecology, and human systems",
        "chapters": {
            "3": {"title": "The Chemical Foundation of Life", "topics": ["atoms", "molecules", "chemistry"]},
            "4": {"title": "Carbon", "topics": ["organic chemistry", "carbon compounds"]},
            "5": {"title": "Biological Macromolecules", "topics": ["proteins", "carbohydrates", "lipids"]},
            "6": {"title": "Metabolism", "topics": ["energy", "chemical reactions"]},
            "7": {"title": "Cellular Respiration", "topics": ["energy", "cellular processes"]},
            "8": {"title": "Photosynthesis", "topics": ["plants", "energy", "chemical reactions"]},
            "9": {"title": "Cell Communication", "topics": ["cells", "signaling"]},
            "10": {"title": "Cell Reproduction", "topics": ["cells", "mitosis", "meiosis"]},
            "11": {"title": "Structure of the Cell", "topics": ["cells", "organelles", "cell parts"]},
            "12": {"title": "Prokaryotes", "topics": ["bacteria", "cells", "classification"]},
            "13": {"title": "Protists", "topics": ["classification", "organisms"]},
            "14": {"title": "Fungi", "topics": ["classification", "organisms"]},
            "15": {"title": "Diversity of Plants", "topics": ["plants", "classification"]},
            "16": {"title": "Diversity of Animals", "topics": ["animals", "classification"]},
            "45": {"title": "Ecosystems", "topics": ["ecosystems", "living systems", "environment"]},
            "46": {"title": "Population Ecology", "topics": ["ecosystems", "populations"]}
        }
    },
    
    "chemistry_2e": {
        "title": "Chemistry 2e",
        "url": "https://openstax.org/details/books/chemistry-2e",
        "pdf_url": "https://openstax.org/books/chemistry-2e/pages/1-introduction",
        "cover_url": "https://d3bxy9euw4e147.cloudfront.net/oscms-prodcms/media/documents/Chemistry_2e_book_card.svg",
        "subjects": ["Chemistry"],
        "grade_level": "High School / College",
        "license": "CC BY 4.0",
        "description": "Complete chemistry textbook covering atoms, periodic table, chemical reactions, and solutions",
        "chapters": {
            "1": {"title": "Essential Ideas", "topics": ["scientific method", "measurement"]},
            "2": {"title": "Atoms, Molecules, and Ions", "topics": ["atoms", "atomic structure", "elements"]},
            "3": {"title": "Electronic Structure and Periodic Properties", "topics": ["atoms", "periodic table", "electrons"]},
            "4": {"title": "Chemical Bonding and Molecular Geometry", "topics": ["atoms", "molecules", "bonding"]},
            "5": {"title": "Advanced Theories of Bonding", "topics": ["molecules", "chemical bonds"]},
            "6": {"title": "Composition of Substances and Solutions", "topics": ["solutions", "mixtures", "concentration"]},
            "7": {"title": "Stoichiometry of Chemical Reactions", "topics": ["chemical reactions", "equations"]},
            "11": {"title": "Solutions and Colloids", "topics": ["solutions", "mixtures", "separation"]},
            "12": {"title": "Kinetics", "topics": ["reaction rates", "chemical change"]},
            "13": {"title": "Fundamental Equilibrium Concepts", "topics": ["chemical reactions", "equilibrium"]},
            "17": {"title": "Electrochemistry", "topics": ["chemical reactions", "electricity"]}
        }
    },
    
    "physics": {
        "title": "Physics",
        "url": "https://openstax.org/details/books/physics",
        "pdf_url": "https://openstax.org/books/physics/pages/1-introduction",
        "cover_url": "https://d3bxy9euw4e147.cloudfront.net/oscms-prodcms/media/documents/Physics_book_card.svg",
        "subjects": ["Physics"],
        "grade_level": "High School / College",
        "license": "CC BY 4.0",
        "description": "Comprehensive physics textbook covering forces, motion, energy, and matter",
        "chapters": {
            "2": {"title": "Kinematics", "topics": ["motion", "velocity", "acceleration"]},
            "3": {"title": "Two-Dimensional Kinematics", "topics": ["motion", "vectors"]},
            "4": {"title": "Dynamics: Force and Newton's Laws", "topics": ["forces", "newton's laws", "motion"]},
            "5": {"title": "Further Applications of Newton's Laws", "topics": ["forces", "friction", "tension"]},
            "6": {"title": "Uniform Circular Motion and Gravitation", "topics": ["forces", "gravity", "circular motion"]},
            "7": {"title": "Work, Energy, and Energy Resources", "topics": ["energy", "work", "power"]},
            "8": {"title": "Linear Momentum and Collisions", "topics": ["momentum", "forces", "motion"]},
            "9": {"title": "Static Equilibrium and Elasticity", "topics": ["forces", "balance"]},
            "10": {"title": "Rotational Motion and Angular Momentum", "topics": ["motion", "rotation"]},
            "15": {"title": "Thermodynamics", "topics": ["heat", "energy", "temperature"]},
            "16": {"title": "Oscillatory Motion and Waves", "topics": ["waves", "motion", "energy"]}
        }
    },
    
    "astronomy": {
        "title": "Astronomy",
        "url": "https://openstax.org/details/books/astronomy",
        "pdf_url": "https://openstax.org/books/astronomy/pages/1-thinking-ahead",
        "cover_url": "https://d3bxy9euw4e147.cloudfront.net/oscms-prodcms/media/documents/Astronomy_book_card.svg",
        "subjects": ["Astronomy", "Space Science"],
        "grade_level": "High School / College",
        "license": "CC BY 4.0",
        "description": "Complete astronomy textbook covering the solar system, stars, galaxies, and the universe",
        "chapters": {
            "1": {"title": "Science and the Universe", "topics": ["universe", "scientific method", "astronomy"]},
            "2": {"title": "Observing the Sky", "topics": ["sky patterns", "constellations", "celestial sphere"]},
            "3": {"title": "Orbits and Gravity", "topics": ["gravity", "planetary motion", "forces"]},
            "4": {"title": "Earth, Moon, and Sky", "topics": ["earth", "moon", "sky patterns"]},
            "6": {"title": "Astronomical Instruments", "topics": ["telescopes", "technology", "observations"]},
            "7": {"title": "Other Worlds", "topics": ["planets", "solar system"]},
            "8": {"title": "Earth as a Planet", "topics": ["earth", "geology", "atmosphere"]},
            "9": {"title": "Cratered Worlds", "topics": ["moon", "mercury", "impacts"]},
            "10": {"title": "Earthlike Planets", "topics": ["venus", "mars", "planets"]},
            "11": {"title": "The Giant Planets", "topics": ["jupiter", "saturn", "gas giants"]},
            "12": {"title": "Rings, Moons, and Pluto", "topics": ["planetary systems", "moons"]},
            "13": {"title": "Comets and Asteroids", "topics": ["solar system", "asteroids", "comets"]},
            "14": {"title": "Cosmic Samples and the Origin of the Solar System", "topics": ["solar system formation", "meteorites"]}
        }
    },
    
    "chemistry_atoms_first": {
        "title": "Chemistry: Atoms First 2e",
        "url": "https://openstax.org/details/books/chemistry-atoms-first-2e",
        "pdf_url": "https://openstax.org/books/chemistry-atoms-first-2e/pages/1-introduction",
        "cover_url": "https://d3bxy9euw4e147.cloudfront.net/oscms-prodcms/media/documents/ChemistryAtomsFirst2e_book_card.svg",
        "subjects": ["Chemistry"],
        "grade_level": "High School / College",
        "license": "CC BY 4.0",
        "description": "Chemistry textbook organized with atomic structure first, ideal for understanding periodic table",
        "chapters": {
            "2": {"title": "Atoms, Molecules, and Ions", "topics": ["atoms", "atomic structure", "ions"]},
            "3": {"title": "Electronic Structure and Periodic Properties", "topics": ["periodic table", "electrons", "elements"]},
            "4": {"title": "Chemical Bonding and Molecular Geometry", "topics": ["bonding", "molecules"]},
            "9": {"title": "Stoichiometry of Chemical Reactions", "topics": ["chemical reactions", "equations"]},
            "10": {"title": "Liquids and Solids", "topics": ["states of matter", "phase changes"]},
            "11": {"title": "Solutions and Colloids", "topics": ["solutions", "mixtures", "concentration"]}
        }
    },
    
    "concepts_biology": {
        "title": "Concepts of Biology",
        "url": "https://openstax.org/details/books/concepts-biology",
        "pdf_url": "https://openstax.org/books/concepts-biology/pages/1-introduction",
        "cover_url": "https://d3bxy9euw4e147.cloudfront.net/oscms-prodcms/media/documents/ConceptsofBiology_book_card.svg",
        "subjects": ["Biology"],
        "grade_level": "High School",
        "license": "CC BY 4.0",
        "description": "Introductory biology designed for one-semester courses, covers essential biology concepts",
        "chapters": {
            "3": {"title": "Chemistry of Life", "topics": ["atoms", "molecules", "chemistry", "water"]},
            "4": {"title": "Cell Structure and Function", "topics": ["cells", "organelles", "cell membrane"]},
            "5": {"title": "How Cells Obtain Energy", "topics": ["cellular respiration", "photosynthesis", "energy"]},
            "13": {"title": "Diversity of Life", "topics": ["classification", "organisms", "taxonomy"]},
            "15": {"title": "Animal Body Systems", "topics": ["body systems", "organs", "living systems"]},
            "16": {"title": "Population and Community Ecology", "topics": ["ecosystems", "populations", "communities"]}
        }
    }
}

# NSW Stage 4 Focus Areas to OpenStax Chapter Mapping
NSW_TOPIC_MAPPINGS = {
    "SC4-OTU-01": {  # Observing the Universe
        "nesa_name": "Observing the Universe",
        "keywords": ["space", "universe", "solar system", "planets", "stars", "astronomy", "sky", "telescope"],
        "textbook_chapters": [
            {"book": "astronomy", "chapters": [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14], "relevance": "high"},
        ]
    },
    
    "SC4-FRC-01": {  # Forces
        "nesa_name": "Forces",
        "keywords": ["force", "forces", "motion", "gravity", "friction", "push", "pull", "newton", "contact", "non-contact"],
        "textbook_chapters": [
            {"book": "physics", "chapters": [4, 5, 6, 8, 9], "relevance": "high"},
            {"book": "astronomy", "chapters": [3], "relevance": "medium"}
        ]
    },
    
    "SC4-LW-02": {  # Cells and Classification
        "nesa_name": "Cells and Classification",
        "keywords": ["cell", "cells", "organelle", "organism", "classification", "taxonomy", "prokaryote", "eukaryote", "animal", "plant"],
        "textbook_chapters": [
            {"book": "biology_2e", "chapters": [10, 11, 12, 13, 14, 15, 16], "relevance": "high"},
            {"book": "concepts_biology", "chapters": [4, 13], "relevance": "high"}
        ]
    },
    
    "SC4-SOL-01": {  # Solutions and Mixtures
        "nesa_name": "Solutions and Mixtures",
        "keywords": ["solution", "mixture", "solubility", "dissolve", "solvent", "solute", "concentration", "separation", "filtration"],
        "textbook_chapters": [
            {"book": "chemistry_2e", "chapters": [6, 11], "relevance": "high"},
            {"book": "chemistry_atoms_first", "chapters": [11], "relevance": "high"}
        ]
    },
    
    "SC4-LW-01": {  # Living Systems
        "nesa_name": "Living Systems",
        "keywords": ["ecosystem", "living system", "body system", "energy flow", "food chain", "photosynthesis", "respiration", "organs"],
        "textbook_chapters": [
            {"book": "biology_2e", "chapters": [7, 8, 45, 46], "relevance": "high"},
            {"book": "concepts_biology", "chapters": [5, 15, 16], "relevance": "high"}
        ]
    },
    
    "SC4-PRT-01": {  # Periodic Table and Atomic Structure
        "nesa_name": "Periodic Table and Atomic Structure",
        "keywords": ["atom", "atomic", "element", "periodic table", "electron", "proton", "neutron", "compound", "molecule"],
        "textbook_chapters": [
            {"book": "chemistry_2e", "chapters": [2, 3, 4], "relevance": "high"},
            {"book": "chemistry_atoms_first", "chapters": [2, 3, 4], "relevance": "high"},
            {"book": "biology_2e", "chapters": [3], "relevance": "medium"},
            {"book": "concepts_biology", "chapters": [3], "relevance": "medium"}
        ]
    },
    
    "SC4-CHG-01": {  # Change
        "nesa_name": "Change",
        "keywords": ["chemical change", "physical change", "reaction", "reversible", "irreversible", "conservation of mass"],
        "textbook_chapters": [
            {"book": "chemistry_2e", "chapters": [7, 12, 13, 17], "relevance": "high"},
            {"book": "chemistry_atoms_first", "chapters": [9, 10], "relevance": "high"},
            {"book": "physics", "chapters": [15], "relevance": "medium"}
        ]
    },
    
    "SC4-DAT-01": {  # Data Science
        "nesa_name": "Data Science",
        "keywords": ["data", "graph", "analysis", "measurement", "investigation", "scientific method", "variables"],
        "textbook_chapters": [
            {"book": "chemistry_2e", "chapters": [1], "relevance": "medium"},
            {"book": "astronomy", "chapters": [1], "relevance": "medium"}
        ]
    }
}


def get_textbooks_for_topic(topic_keywords):
    """
    Find relevant OpenStax textbooks based on topic keywords
    Returns list of textbook recommendations with chapters
    """
    topic_lower = topic_keywords.lower()
    recommendations = []
    
    # Check NSW focus area mappings first
    for focus_area, mapping in NSW_TOPIC_MAPPINGS.items():
        if any(keyword in topic_lower for keyword in mapping['keywords']):
            for textbook_ref in mapping['textbook_chapters']:
                book_key = textbook_ref['book']
                if book_key in OPENSTAX_TEXTBOOKS:
                    book = OPENSTAX_TEXTBOOKS[book_key]
                    recommendations.append({
                        'title': book['title'],
                        'url': book['url'],
                        'pdf_url': book['pdf_url'],
                        'cover_url': book['cover_url'],
                        'description': book['description'],
                        'focus_area': mapping['nesa_name'],
                        'recommended_chapters': textbook_ref['chapters'],
                        'relevance': textbook_ref['relevance']
                    })
    
    # Remove duplicates and sort by relevance
    unique_recommendations = []
    seen_titles = set()
    for rec in recommendations:
        if rec['title'] not in seen_titles:
            seen_titles.add(rec['title'])
            unique_recommendations.append(rec)
    
    # Sort by relevance (high first)
    unique_recommendations.sort(key=lambda x: 0 if x['relevance'] == 'high' else 1)
    
    return unique_recommendations[:3]  # Return top 3 most relevant


def get_chapter_details(book_key, chapter_num):
    """Get specific chapter information from a textbook"""
    if book_key in OPENSTAX_TEXTBOOKS:
        book = OPENSTAX_TEXTBOOKS[book_key]
        chapters = book.get('chapters', {})
        if str(chapter_num) in chapters:
            return {
                'book_title': book['title'],
                'chapter_title': chapters[str(chapter_num)]['title'],
                'chapter_url': f"{book['pdf_url']}/{chapter_num}-introduction",
                'topics': chapters[str(chapter_num)]['topics']
            }
    return None


def format_textbook_recommendation(textbook_rec):
    """Format textbook recommendation for display"""
    chapters_text = ""
    if textbook_rec.get('recommended_chapters'):
        chapter_nums = textbook_rec['recommended_chapters'][:3]  # Show first 3
        chapters_text = f"Recommended chapters: {', '.join(map(str, chapter_nums))}"
    
    return {
        'title': textbook_rec['title'],
        'description': textbook_rec['description'],
        'url': textbook_rec['url'],
        'pdf_url': textbook_rec['pdf_url'],
        'chapters': chapters_text,
        'focus_area': textbook_rec.get('focus_area', ''),
        'type': 'OpenStax Free Textbook',
        'license': 'CC BY 4.0 - Free to use and share'
    }
