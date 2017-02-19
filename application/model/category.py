from . import db  # , Model


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    posts = db.relationship('Post', backref='Post', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %s>' % self.name

    def save(self):
        db.session.add(self)
        db.session.commit()
