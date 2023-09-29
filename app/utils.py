from scholarly import scholarly
#from scholarly import ProxyGenerator

#pg = ProxyGenerator()
#success = pg.FreeProxies()
#scholarly.use_proxy(pg)

def search_google_scholar(query, n = 10):
    search_query = scholarly.search_pubs(query)
    professors = []
    count = 0
    while count < n:
        paper = next(search_query)
        authors = paper['author_id']
        if len(authors)!=0:
            last_author = authors[-1]
            if last_author != '':
                #search that author based on the author id
                last_author_information = scholarly.search_author_id(last_author)
                if '.edu' in last_author_information['email_domain']:
                    try:
                        image_url = last_author_information['url_picture']
                    except:
                        image_url = '#'
                    try:
                        homepage = last_author_information['homepage']
                    except:
                        homepage = '#'
                    #check if the author is already in the list
                    if last_author_information['name'] not in [x['name'] for x in professors]:
                        professors.append({
                            'name': last_author_information['name'],
                            'affiliation':last_author_information['affiliation'],
                            'homepage': homepage,
                            'image_url': image_url,
                            'interests': ', '.join(str(x) for x in last_author_information['interests'])
                        })
                        count+=1
    return professors

#%%
