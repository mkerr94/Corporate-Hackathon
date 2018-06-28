from app import db

class Vote(db.Model):
    __tablename__ = 'vote'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    text = db.Column(db.String(1000))

    def __repr__(self):
        return '<Vote user_id = {}, post_id = {}, text = {}>'\
            .format(self.user_id, self.post_id, self.text)
