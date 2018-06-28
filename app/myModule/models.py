from app import db

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Date())
    title = db.Column(db.String(500))
    description = db.Column(db.String(1000), unique = True)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)

    def __repr__(self):
        return '<Post id = {}, timestamp = {}, title = {}, description = {}, upvotes={}, downvotes = {}>'\
            .format(self.id, self.timestamp, self.title, self.description, self.upvotes, self.downvotes)

class Vote(db.Model):
    __tablename__ = 'vote'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    text = db.Column(db.String(1000))

    def __repr__(self):
        return '<Vote user_id = {}, post_id = {}, text = {}>'\
            .format(self.user_id, self.post_id, self.text)


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key = True)
    id_post = db.Column(db.Integer, db.ForeignKey('post.id'))
    text = db.Column(db.String(1000))


    def __repr__(self):
        return '<Comment id_comment = {}, id_post = {}, text = {}>'\
            .format(self.id, self.id_post, self.text)

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(500))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


    def __repr__(self):
        return '<Cateory id = {}, name = {}, post_id = {}>'\
            .format(self.id, self.name, self.post_id)