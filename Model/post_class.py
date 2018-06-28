
from Model.app import db

class Post(db.Model):
    __tablename__ = 'post'

    id_post = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.Date())
    title = db.Column(db.String(500))
    description = db.Column(db.String(1000), unique = True)
    votes_number = db.Column(db.Integer)


    def __repr__(self):
        return '<User {}>'.format(self.username)
