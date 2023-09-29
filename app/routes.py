from flask import Blueprint, render_template, request
from .utils import SEMANTIC_SCHOLAR_PAPER_API_URL, SEMANTIC_SCHOLAR_AUTHOR_API_URL, CROSSREF_API_URL, is_full_name
from .config import SEMANTIC_API_KEY
import requests
import re

main = Blueprint('main', __name__)
if SEMANTIC_API_KEY is not None:
    print("using API key for semantic scholar")
@main.route('/')
def home():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    authors = []
    seen_auth = []
    for i in range(5):
        while(True):
            query = request.form['query']

            # Step 1: Fetch papers from Semantic Scholar
            if SEMANTIC_API_KEY is not None:
                response = requests.get(f"{SEMANTIC_SCHOLAR_PAPER_API_URL}?query={query}&fields=authors&year=2018-2023&offset={10*i}", headers={"x-api-key":SEMANTIC_API_KEY})
            else:
                response = requests.get(f"{SEMANTIC_SCHOLAR_PAPER_API_URL}?query={query}&fields=authors&year=2018-2023&offset={10*i}")
            data = response.json()
            try:
                if 'Too Many Requests.' in data['message']:
                    continue
            except:
                break
        try:
            if data['data']:
                pass
        except:
            continue
        for item in data["data"]:
            # Step 2: Fetch the last author's details using authorId
            try:
                last_author = item["authors"][-1]
            except:
                continue
            try:
                author_response = requests.get(f"{SEMANTIC_SCHOLAR_AUTHOR_API_URL}/{last_author['authorId']}?fields=url,name,affiliations,homepage")
                author_data = author_response.json()
                if author_data['error'] != '':
                    continue
            except:
                author_response = requests.get(f"{SEMANTIC_SCHOLAR_AUTHOR_API_URL}/{last_author['authorId']}?fields=url,name,affiliations,homepage")
                author_data = author_response.json()

            affiliation = None
            print(author_data)
            # Check if 'affiliations' is available for the author
            if 'affiliations' in author_data and author_data['affiliations']:
                affiliation = author_data["affiliations"][0]

            # Step 3 & 4: If no affiliations but full name available, search in CrossRef
            elif is_full_name(author_data['name']):
                crossref_response = requests.get(f"{CROSSREF_API_URL}?query.author={author_data['name']}&filter=has-affiliation:true&rows=1")
                crossref_data = crossref_response.json()
                if crossref_data["message"]["total-results"] > 0:
                    paper = crossref_data["message"]["items"][0]
                    for a in paper["author"]:
                        if "affiliation" in a:
                            try:
                                affiliation = re.sub(r'\d+', '', a["affiliation"][0]["name"]).strip()
                            except:
                                affiliation = False
                            break

            if affiliation and author_data["name"] not in seen_auth:
                if author_data.get("homepage", "") == None:
                    homepage = author_data['url']
                else:
                    homepage = author_data.get("homepage", "")
                authors.append({
                    "name": author_data["name"],
                    "affiliation": affiliation,
                    "url": author_data.get("url", ""),
                    "homepage": homepage
                })
                seen_auth.append(author_data["name"])

    return render_template('results.html', authors=authors)
#%%
