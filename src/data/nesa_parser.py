"""
Enhanced NESA document parser - extracts structured curriculum content
"""
from docx import Document
from typing import Dict, List
import json


def parse_teaching_advice_doc(filepath: str) -> Dict:
    """Parse NESA syllabus support document to extract teaching advice for all focus areas"""
    doc = Document(filepath)
    content = {}
    current_focus_area = None
    current_section = None
    section_items = []
    
    for para in doc.paragraphs:
        text = para.text.strip()
        style = para.style.name if para.style else ""
        
        # Detect focus area headings (Heading 3)
        if style == "Heading 3" and "Teaching advice for" in text:
            # Save previous section
            if current_focus_area and current_section and section_items:
                if current_focus_area not in content:
                    content[current_focus_area] = {}
                content[current_focus_area][current_section] = section_items.copy()
            
            # Extract focus area name and filter to Stage 4 only
            focus_area = text.replace("Teaching advice for", "").strip()
            if focus_area in ["Observing the Universe", "Forces", "Cells and classification",
                            "Solutions and mixtures", "Living systems", 
                            "Periodic table and atomic structure", "Change", "Data Science 1"]:
                current_focus_area = focus_area
                section_items = []
                current_section = None
            else:
                current_focus_area = None
        
        # Detect section headings (Heading 5)
        elif current_focus_area and style == "Heading 5":
            # Save previous section
            if current_section and section_items:
                if current_focus_area not in content:
                    content[current_focus_area] = {}
                content[current_focus_area][current_section] = section_items.copy()
            
            current_section = text.lower()
            section_items = []
        
        # Collect section content
        elif current_focus_area and current_section:
            if style == "List Paragraph" and text:
                section_items.append(text)
            elif style == "Normal" and text and not text.startswith("The following"):
                # Add paragraph text as a single item
                if section_items and not section_items[-1].endswith('.'):
                    section_items[-1] += " " + text
                else:
                    section_items.append(text)
    
    # Save last section
    if current_focus_area and current_section and section_items:
        if current_focus_area not in content:
            content[current_focus_area] = {}
        content[current_focus_area][current_section] = section_items
    
    return content


def build_nesa_content_database():
    """Build comprehensive NESA content database for all Stage 4 focus areas"""
    
    # Parse teaching advice
    support_path = "attached_assets/NESA - science_7_10_2023 syllabus support (S4, S5, LS)_1762345248825.docx"
    teaching_content = parse_teaching_advice_doc(support_path)
    
    # Structure the database
    nesa_db = {}
    
    for focus_area, sections in teaching_content.items():
        nesa_db[focus_area] = {
            'key_ideas': sections.get('key ideas', []),
            'investigations': sections.get('investigations', []),
            'background_knowledge': sections.get('background knowledge', []),
            'skills': sections.get('skills', []),
            'depth_studies': sections.get('suggested depth study', []),
            'in_context': sections.get('in context', [])
        }
    
    return nesa_db


if __name__ == '__main__':
    # Test the parser
    db = build_nesa_content_database()
    
    print("NESA Content Database Created")
    print("=" * 70)
    for area, data in db.items():
        print(f"\n{area}:")
        print(f"  Key Ideas: {len(data['key_ideas'])} items")
        print(f"  Investigations: {len(data['investigations'])} items")
        print(f"  Background Knowledge: {len(data['background_knowledge'])} items")
        
        if data['investigations']:
            print(f"\n  Sample Investigation:")
            print(f"    • {data['investigations'][0][:100]}...")
    
    # Save to JSON for inspection
    with open('nesa_content_test.json', 'w') as f:
        json.dump(db, f, indent=2)
    print("\n\nFull content saved to nesa_content_test.json")
