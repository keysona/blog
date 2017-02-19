from unittest import TestCase as BaseTestCase
from application import create_app


class TestCase(BaseTestCase):
    def setUp(self):
        self.app = create_app().test_client()
