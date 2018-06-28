from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Test User'}
    return render_template('index.html.j2', title='Home', user=user)

@app.route('/post')
def post():
    return render_template('post.html.j2', title='Post')

@app.route('/create')
def create_post():
    return render_template('create_post.html.j2', title='Create')
