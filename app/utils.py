from scholarly import scholarly

def search_google_scholar(query):
    search_query = scholarly.search_pubs(query)
    papers = [next(search_query) for _ in range(10)]
    
    professors = []
    for paper in papers:
        authors = paper.bib.get('author', '').split(', ')
        if authors:
            last_author = authors[-1]
            affiliations = paper.bib.get('eprint', '').split('@')
            uni_name = affiliations[1] if len(affiliations) > 1 else ""
            if ".edu" in uni_name:
                professors.append(last_author)

    return professors