SEMANTIC_SCHOLAR_PAPER_API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
SEMANTIC_SCHOLAR_AUTHOR_API_URL = "https://api.semanticscholar.org/graph/v1/author"
CROSSREF_API_URL = "https://api.crossref.org/works"

def is_full_name(name):
    parts = name.split(' ')
    # Check if the first part is a single initial (e.g., "A." or "A")
    if len(parts[0]) <= 2 and '.' in parts[0]:
        return False
    return True