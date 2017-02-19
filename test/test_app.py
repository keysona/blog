from . import TestCase


class TestApplication(TestCase):
    def test_index(self):
        rv = self.app.get('/')
        assert b'Hello' in rv.data
