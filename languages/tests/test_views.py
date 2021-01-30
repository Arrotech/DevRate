import json
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from ..models import Language
from ..serializers import LanguageSerializer
from .dummy import add_language, add_invalid_language
from .base_test import BaseTest


class TestLanguages(TestCase):
    """ Test module for inserting a new puppy """

    def test_add_new_language(self):
        response = self.client.post(reverse('add_language'),
                                    data=json.dumps(add_language),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_invalid_language(self):
        response = self.client.post(reverse('add_language'),
                                    data=json.dumps(add_invalid_language),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
