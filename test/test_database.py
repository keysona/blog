from . import TestCase, db, data
from application.model import Category, Tag, Post, User


class TestDatabase(TestCase):
    def test_category(self):
        with self.app.app_context():
            # query data
            category = Category.query.filter_by(name=data['Category'][0]['name']).first()
            self.assertIsNotNone(category)

            # delete data
            category.delete()
            category = Category.query.filter_by(name=data['Category'][0]['name']).first()
            self.assertIsNone(category)

    def test_tag(self):
        with self.app.app_context():
            # query data
            tag = Tag.query.filter_by(name=data['Tag'][0]['name']).first()
            self.assertIsNotNone(tag)

            # delete data
            tag.delete()
            tag = Tag.query.filter_by(name=data['Tag'][0]['name']).first()
            self.assertIsNone(tag)

    def test_post(self):
        with self.app.app_context():
            # query data
            post = Post.query.filter_by(title=data['Post'][0]['title']).first()
            self.assertIsNotNone(post)

            # delete data
            post.delete()
            post = Post.query.filter_by(title=data['Post'][0]['title']).first()
            self.assertIsNone(post)

            # def test_get_
