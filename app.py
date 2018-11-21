import os
from flask import Flask
from flask_login import LoginManager, login_required
from flask import send_from_directory
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import request
from werkzeug.urls import url_parse
#from app import db
#from app.forms import RegistrationForm

app = Flask(__name__)
Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    #...
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    # ...
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@login_required
@app.route('/profile.html')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':

    app.run(debug=True, port=33507)

