def clean_tags(tags):
    """Remove duplicates and empty tags while preserving order."""
    if not tags:
        return []
    
    seen = set()
    cleaned = []
    
    for tag in tags:
        tag = tag.strip()
        if tag and tag not in seen:
            seen.add(tag)
            cleaned.append(tag)
            
    return cleaned