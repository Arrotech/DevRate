from django.test import Client


class BaseTest:

    def setUp(self):
        self.client = Client()
