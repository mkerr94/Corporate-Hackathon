from flask import Flask
from flask import render_template, request, redirect
import datetime
import Post


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql2245027:hR8*eV4!@sql2.freemysqlhosting.net/sql2245027'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Test User'}
    posts = []
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/searchPost')
def searchPost():
    keyword = request.args.get('keyword')
    posts = []
    if '*' in keyword or '_' in keyword:
        looking_for = keyword.replace('_', '__') \
            .replace('*', '%') \
            .replace('?', '_')
    else:
        looking_for = '%{0}%'.format(keyword)
    posts += Post.query.filter_by(Post.title.ilike(looking_for)).all()
    posts += Post.query.filter_by(Post.description.ilike(looking_for)).all()
    posts = set(posts)
    return posts

@app.route('/searchCategory')
def searchCategory():
    keyword = request.args.get('keyword')
    if '*' in keyword or '_' in keyword:
        looking_for = keyword.replace('_', '__') \
            .replace('*', '%') \
            .replace('?', '_')
    else:
        looking_for = '%{0}%'.format(keyword)
    categories = Post.query.filter_by(Post.title.ilike(looking_for)).all()
    return categories

@app.route('/createPost', methods = ['POST'])
def createPost():
    post = Post(timestamp=datetime.datetime.now(),
                title=request.form['title'],
                description=request.form['description'],
                upvotes=0,
                downvotes=0)
    addToDB(post)
    return redirect(url_for('index'))

@app.route('/createPost', methods = ['POST'])
def vote():
    vote = Vote(user_id=request.form['user_id'],
                post_id=request.form['post_id'],
                vote=request.form['vote'])
    post = Post.query.filter_by(id=request.form['post_id']).first()
    if vote:
        post.upvote += 1
    else:
        post.downvote += 1
    addToDB(vote)


def addToDB(comment):
    db.session.add(comment)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)