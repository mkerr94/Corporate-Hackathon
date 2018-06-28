from Model.app import db



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
