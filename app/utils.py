from scholarly import scholarly

def search_google_scholar(query):
    search_query = scholarly.search_pubs(query)
    papers = [next(search_query) for _ in range(20)]
    professors = []
    for paper in papers:
        authors = paper['author_id']
        if len(authors)!=0:
            last_author = authors[-1]
            if last_author != '':
                #search that author based on the author id
                last_author_information = scholarly.search_author_id(last_author)
                #print(last_author_information.keys())
                if '.edu' in last_author_information['email_domain'] and last_author_information['name'] not in professors:
                    professors.append(last_author_information['name'])
    return professors
