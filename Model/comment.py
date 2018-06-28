from Model.app import db

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key = True)
    id_post = db.Column(db.Integer, db.ForeignKey('post.id'))
    text = db.Column(db.String(1000))


    def __repr__(self):
        return '<Comment id_comment = {}, id_post = {}, text = {}>'\
            .format(self.id, self.id_post, self.text)
