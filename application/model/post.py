from datetime import datetime
from . import db

post_tag = db.Table('post_tag',
                    db.Column('tag_id', db.Integer(),
                              db.ForeignKey('tag.id')),
                    db.Column('post_id', db.Integer(),
                              db.ForeignKey('post.id'))
                    )


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    pub_date = db.Column(db.DateTime())
    modified_date = db.Column(db.DateTime())
    title = db.Column(db.String(255), unique=True)
    article = db.Column(db.Text())
    hit_count = db.Column(db.Integer())
    slug = db.Column(db.String(255), unique=True)
    tags = db.relationship('Tag', secondary=post_tag,
                           backref=db.backref('posts', lazy='dynamic'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, article, slug, category):
        self.title = title
        self.article = article
        self.slug = slug
        self.category = category
        self.hit_count = 0
        self.pub_date = self.modified_date = datetime.now()

    def __repr__(self):
        return '<Article %s>' % self.title

    def add_hit_count(self):
        self.hit_count += 1
        self.save()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
