from flask import url_for
from . import TestCase


class TestApplication(TestCase):

    def test_index(self):
        with self.app.app_context():
            # rv = self.client.get(url_for('/'))
            # self.assertEqual(rv.status_code, 200)

            rv = self.client.get(url_for('blog.index'))
            print(url_for(('blog.index')))
            self.assertEqual(rv.status_code, 200)

            rv = self.client.get('/index/page/1')
            self.assertEqual(rv.status_code, 301)
