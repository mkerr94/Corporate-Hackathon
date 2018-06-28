from flask import Blueprint, render_template, request, redirect, url_for
import datetime
from app.myModule.models import Comment, Vote, Post, Category
from app import db

myModule = Blueprint('myModule', __name__)
user = {'username': 'Test User'}

@myModule.route('/')
@myModule.route('/index')
def index():
    posts = Post.query.order_by(Post.upvotes - Post.downvotes).all()
    categories = Category.query.order_by(Category.id).limit(10).all()
    # print("---------------" +str(posts))
    return render_template('index.html.j2', title='Home', user=user, posts=posts, categories=categories)

@myModule.route('/post')
def post():
    id = request.args.get('id')
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html.j2', post=post)


@myModule.route('/create')
def create():
    return render_template('create_post.html.j2')

@myModule.route('/searchPost')
def searchPost():
    keyword = request.args.get('keyword')
    posts = []
    if '*' in keyword or '_' in keyword:
        looking_for = keyword.replace('_', '__') \
            .replace('*', '%') \
            .replace('?', '_')
    else:
        looking_for = '%{0}%'.format(keyword)
    posts += Post.query.filter(Post.title.ilike(looking_for)).all()
    posts += Post.query.filter(Post.description.ilike(looking_for)).all()
    posts = set(posts)
    return render_template('index.html.j2', title='Home', user=user, posts=posts)

@myModule.route('/searchCategory')
def searchCategory():
    keyword = request.args.get('keyword')
    if '*' in keyword or '_' in keyword:
        looking_for = keyword.replace('_', '__') \
            .replace('*', '%') \
            .replace('?', '_')
    else:
        looking_for = '%{0}%'.format(keyword)
    categories = Post.query.filter(Post.title.ilike(looking_for)).all()
    return categories

@myModule.route('/searchByCategory')
def searchByCategory():
    categories = request.args.get('keyword')
    categories = categories.split(",")
    posts_ids = []
    for c in categories:
        posts_ids += Category.query.filter_by(name=c).all()

    posts = []
    for id in posts_ids:
        posts += Post.query.filter_by(id=id).all()

    return posts


@myModule.route('/createPost', methods = ['POST'])
def createPost():
    post = Post(timestamp=datetime.datetime.now(),
                title=request.form['title'],
                description=request.form['description'],
                upvotes=0,
                downvotes=0)
    addToDB(post)
    return redirect(url_for('.index'))

@myModule.route('/postComment', methods = ['POST'])
def postComment():
    comment = Comment(user_id=request.form['user_id'],
                post_id=request.form['post_id'],
                vote=request.form['text'])
    addToDB(comment)
    return redirect(url_for('.index'))

@myModule.route('/vote', methods = ['POST'])
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


def addToDB(item):
    db.session.add(item)
    db.session.commit()
