from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import render_template

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Test User'}
    return render_template('index.html', title='Home', user=user)