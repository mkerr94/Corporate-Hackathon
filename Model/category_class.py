from app import db

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(500))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


    def __repr__(self):
        return '<Cateory id = {}, name = {}, post_id = {}>'\
            .format(self.id, self.name, self.post_id)
