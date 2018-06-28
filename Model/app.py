from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import render_template
app = Flask(__name__)
db = SQLAlchemy(app)

#
# def add_posts():
#     for i in range(100):
#         p = Post(id = i,
#                  timestamp = date.today(),
#                  title = 'title ' + str(i),
#                  description = 'description ' + str(i),
#                  upvotes = gauss(1, 100, 2),
#                  downvotes = gauss(1, 100, 2))
#
#         db.session.add(p)
#
#     db.session.commit()

@app.route('/')
@app.route('/index')
def index():
    add_posts()
    user = {'username': 'Test User'}
    return render_template('index.html', title='Home', user=user)