from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import datetime
from app.myModule.models import Comment, Vote, Post, Category
from app import db

myModule = Blueprint('myModule', __name__)
userlist = ["Bob Murray", "John Madden", "Sarah Kirkhope", "Geoff Freeman", "Jenny Hawlith", "Karina White"]
user = 0

@myModule.route('/')
@myModule.route('/index')
def index():
    posts = Post.query.order_by(Post.upvotes - Post.downvotes).limit(6).all()
    categories = Category.query.order_by(Category.id).limit(10).all()
    return render_template('index.html.j2', title='Home', user=userlist[user], posts=posts, categories=categories)

@myModule.route('/post')
def post():
    id = request.args.get('id')
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html.j2', user=userlist[user], post=post)

@myModule.route('/create')
def create():
    return render_template('create_post.html.j2', user=userlist[user])

@myModule.route('/changeUser') # Super secret dev thing!
def changeUser():
    from random import randint
    random_user = randint(0, len(userlist) - 1)
    global user
    user = random_user
    return redirect(url_for('.index'))

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
                author=userlist[user],
                description=request.form['description'],
                upvotes=0,
                downvotes=0)
    addToDB(post)

    cat_list = parseCategories(request.form['categories'])
    for cat in cat_list:
        category = Category(name=cat,
                            post_id=post.id)
        addToDB(category)

    return redirect(url_for('.index'))

def parseCategories(list_string):
    # Assume proper input validation is accomplished.
    cat_list = list_string.split(',')
    for i in range(0, len(cat_list)):
        cat_list[i] = cat_list[i].strip() # Trim whitespaces
    return cat_list

@myModule.route('/postComment', methods = ['POST'])
def postComment():
    comment = Comment(user_id=request.form['user_id'],
                post_id=request.form['post_id'],
                vote=request.form['text'])
    addToDB(comment)
    return redirect(url_for('.index'))

@myModule.route('/vote', methods = ['POST'])
def vote():
    user_id=request.form['user_id']
    post_id=request.form['post_id']
    vote_type=request.form['vote_type']
    query = Vote.query.filter((Vote.user_id == user_id) & (Vote.post_id == post_id))
    existing_vote = query.first()

    post = Post.query.filter_by(id=request.form['post_id']).first()
    if (post is None): raise Exception("Somehow, the id couldn't be found.")

    json = None

    if (existing_vote is None):
        # The user voted on this post for the first time.
        vote = Vote(user_id=user_id,
                    post_id=post_id,
                    text=vote_type)
        if (int(vote_type) != 0):
            post.upvotes += 1
        else:
            post.downvotes += 1
        addToDB(vote)
        result = 1
    else:
        # The user had already voted on this post.
        if (existing_vote.text == vote_type): # Tried to repeat an action.
            if (int(vote_type) != 0):
                post.upvotes -= 1
            else:
                post.downvotes -= 1
            result = -1
            query.delete()
        else:
            existing_vote.text = vote_type
            if (int(vote_type) != 0):
                post.upvotes += 1
                post.downvotes -= 1
            else:
                post.upvotes -= 1
                post.downvotes += 1
            result = 2

    print(post.upvotes)
    print(post.downvotes)
    
    db.session.commit()
    return jsonify(result=result)

def addToDB(item):
    db.session.add(item)
    db.session.commit()
