from flask import render_template, request
from app import app
from app.utils import search_google_scholar

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        results = search_google_scholar(query)
    return render_template('index.html', professors=results)