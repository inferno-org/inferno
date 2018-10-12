import os
from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/')
def start():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/mission.html')
def mission():
    return render_template('mission.html')

@app.route('/teams.html')
def teams():
    return render_template('teams.html')

@app.route('/sponsors.html')
def sponsors():
    return render_template('sponsors.html')

@app.route('/blaze.html')
def blaze():
    return render_template('blaze.html')

@app.route('/ember.html')
def ember():
    return render_template('ember.html')

@app.route('/ragnarok.html')
def ragnarok():
    return render_template('ragnarok.html')

if __name__ == '__main__':

    app.run(debug=True, port=33507)

