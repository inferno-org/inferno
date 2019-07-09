import os
from flask import Flask, send_from_directory, render_template, request, redirect, url_for, session, flash
from functools import wraps
from flask_login import LoginManager, login_required
from flask_bootstrap import Bootstrap
from werkzeug.urls import url_parse
#from app import db
#from app.forms import RegistrationForm

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'NW2clYRvJVwBEfoIqvoJnQGgufgwreY9'



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/')
def start():
    return render_template('index.html')

@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')

@app.route('/blaze')
def blaze():
    return render_template('blaze.html')

@app.route('/ember')
def ember():
    return render_template('ember.html')

@app.route('/streams')
def streams():
    return render_template('streams.html')

@app.route('/ragnarok')
def ragnarok():
    return render_template('ragnarok.html')

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('home'))
    return render_template('login', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('home'))
if __name__ == '__main__':

    app.run(debug=True, port=33507)

