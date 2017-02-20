from flask import url_for
from . import TestCase, db, data
from application.model import Category, Tag, Post, User


class TestModel(TestCase):
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

    def test_post_add_hit_count(self):
        with self.app.app_context():
            post = Post.query.first()
            last_hit_count = post.hit_count
            hit_counts = 3
            for i in range(3):
                rv = self.client.get(url_for('blog.get_post_detail', slug=post.slug))
            post = Post.query.filter_by(slug=post.slug).first()
            self.assertEqual(last_hit_count + hit_counts, post.hit_count)
