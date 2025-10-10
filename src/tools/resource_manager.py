"""
Resource Manager for NSW Science Learning System
Manages educational resources from the catalog
"""
from typing import List, Dict, Any, Optional
import importlib.util
import sys
import os


def load_resource_catalog() -> List[Dict[str, Any]]:
    """Load resources from the resource catalog"""
    try:
        catalog_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'resource_catalog.py')
        
        spec = importlib.util.spec_from_file_location("resource_catalog", catalog_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules["resource_catalog"] = module
        spec.loader.exec_module(module)
        
        return getattr(module, "resources", [])
    except Exception as e:
        print(f"Error loading resource catalog: {e}")
        return []


def find_resources_by_unit(unit: str, resources: List[Dict] = None) -> List[Dict[str, Any]]:
    """Find resources matching a curriculum unit"""
    if resources is None:
        resources = load_resource_catalog()
    
    matching = []
    unit_lower = unit.lower()
    
    for resource in resources:
        alignment = resource.get('Curriculum.Alignment', {})
        resource_unit = alignment.get('Unit', '').lower()
        
        if unit_lower in resource_unit or resource_unit in unit_lower:
            matching.append(resource)
    
    return matching


def find_resources_by_outcome(outcome: str, resources: List[Dict] = None) -> List[Dict[str, Any]]:
    """Find resources matching a learning outcome"""
    if resources is None:
        resources = load_resource_catalog()
    
    matching = []
    
    for resource in resources:
        alignment = resource.get('Curriculum.Alignment', {})
        outcomes = alignment.get('Outcomes', [])
        
        if outcome in outcomes:
            matching.append(resource)
    
    return matching


def find_resources_by_type(resource_type: str, resources: List[Dict] = None) -> List[Dict[str, Any]]:
    """Find resources by type (YouTube Video, Interactive Simulation, etc.)"""
    if resources is None:
        resources = load_resource_catalog()
    
    matching = []
    type_lower = resource_type.lower()
    
    for resource in resources:
        res_type = resource.get('Resource.Type', '').lower()
        if type_lower in res_type:
            matching.append(resource)
    
    return matching


def find_resources_by_query(query: str, resources: List[Dict] = None) -> List[Dict[str, Any]]:
    """Find resources matching a search query"""
    if resources is None:
        resources = load_resource_catalog()
    
    matching = []
    query_lower = query.lower()
    
    for resource in resources:
        # Search in title, description, unit
        title = resource.get('Resource.Title', '').lower()
        description = resource.get('Metadata.Description', '').lower()
        alignment = resource.get('Curriculum.Alignment', {})
        unit = alignment.get('Unit', '').lower()
        
        if (query_lower in title or 
            query_lower in description or 
            query_lower in unit):
            matching.append(resource)
    
    return matching


def get_youtube_videos(query: str = None, resources: List[Dict] = None) -> List[Dict[str, Any]]:
    """Get YouTube video resources"""
    if resources is None:
        resources = load_resource_catalog()
    
    videos = find_resources_by_type("YouTube Video", resources)
    
    if query:
        query_lower = query.lower()
        videos = [v for v in videos if query_lower in v.get('Resource.Title', '').lower() or
                  query_lower in v.get('Metadata.Description', '').lower()]
    
    return videos


def format_resource_for_display(resource: Dict[str, Any]) -> Dict[str, Any]:
    """Format resource for frontend display"""
    return {
        'id': resource.get('ID', ''),
        'title': resource.get('Resource.Title', 'Untitled'),
        'type': resource.get('Resource.Type', 'Resource'),
        'url': resource.get('Resource.URL', ''),
        'description': resource.get('Metadata.Description', ''),
        'source': resource.get('Metadata.Source', ''),
        'difficulty': resource.get('Metadata.Difficulty_Level', 'Core')
    }
