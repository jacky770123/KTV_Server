from flask import Flask, render_template, request, url_for, redirect
from flask_script import Manager, Server
import crawler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        #https://www.youtube.com/results?search_query=%E5%91%8A%E7%99%BD%E6%B0%A3%E7%90%83
        
        song = request.values['song']           #get song's title from index (POST)
        results = crawler.crawlerYT(song)

        return render_template('search.html', results = results, song = song)
    else :
        return redirect(url_for('index'))

@app.route('/wait_list')
def wait_list(name=None):
    return render_template('wait_list.html', name=name)

@app.route('/database')
def database(name=None):
    return render_template('database.html', name=name)


if __name__ == "__main__":
    app.debug = True
    app.run()   #app.run(host='0.0.0.0')