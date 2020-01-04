from flask import Flask, render_template
from flask_script import Manager, Server

app = Flask(__name__)

#url_for('static', filename='style.css')

@app.route("/")
def home():
    return "Hello Flask"

@app.route('/hello')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.debug = True
    app.run()   #app.run(host='0.0.0.0')