from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse
from random import randint
from unittest.mock import patch, MagicMock


class TestViews(TestCase):

    user = AnonymousUser()
    user.id = 1

    @patch("bubbling_firebase_authentication.authentication.FirebaseAuthenticationAnonymous.authenticate",
           MagicMock(return_value=(user, 'some')),)
    def test_get_dummy(self):
        response = self.client.get(reverse('dummy-list'), content_type='application/json', )
        self.assertEqual(response.status_code, 200)

    @patch("bubbling_firebase_authentication.authentication.FirebaseAuthenticationAnonymous.authenticate",
           MagicMock(return_value=(user, 'some')),)
    def test_get_dummy_with_id(self):
        pk = randint(0, 10)
        response = self.client.get(reverse('dummy-list-with-id', args=(pk,)), content_type='application/json')
        self.assertEqual(response.status_code, 200)
