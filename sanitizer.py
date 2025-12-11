import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

def get_interactive_elements(xml_content: str) -> List[Dict]:
    """
    Parses Android Accessibility XML and returns a lean list of interactive elements.
    Calculates center coordinates (x, y) for every clickable element.
    """
    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError:
        print("⚠️ Error parsing XML. The screen might be loading.")
        return []

    elements = []
    
    # Recursively find all nodes
    for node in root.iter():
        # Filter: We only care about elements that are interactive or have information
        is_clickable = node.attrib.get("clickable") == "true"
        is_editable = node.attrib.get("focus") == "true" or node.attrib.get("focusable") == "true"
        text = node.attrib.get("text", "")
        desc = node.attrib.get("content-desc", "")
        resource_id = node.attrib.get("resource-id", "")
        
        # Skip empty layout containers that do nothing
        if not is_clickable and not is_editable and not text and not desc:
            continue
            
        # Parse Bounds: "[140,200][400,350]" -> Center X, Y
        bounds = node.attrib.get("bounds")
        if bounds:
            try:
                # Extract coordinates
                coords = bounds.replace("][", ",").replace("[", "").replace("]", "").split(",")
                x1, y1, x2, y2 = map(int, coords)
                
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                
                element = {
                    "id": resource_id,
                    "text": text or desc,  # Fallback to content-desc if text is empty
                    "type": node.attrib.get("class", "").split(".")[-1],
                    "bounds": bounds,
                    "center": (center_x, center_y),
                    "clickable": is_clickable,
                    "action": "tap" if is_clickable else "read"
                }
                elements.append(element)
            except Exception:
                continue

    return elements