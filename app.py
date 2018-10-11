from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/hello')
def home():
    return "Hello World!"

@app.route('/')
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

if __name__ == '__main__':
    app.run(debug=True, port=33507)

