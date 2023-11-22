from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase


class AuthTestCase(TestCase):
    def test_profile_unauthenticated(self):
        response = self.client.get("/accounts/profile/")

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/accounts/login/?next=/accounts/profile/")

    def test_profile_authenticated(self):
        user = get_user_model().objects.create(
            email="besoin@forfeit.ra", password="medicated*Ka"
        )
        self.client.force_login(user)

        response = self.client.get("/accounts/profile/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "blango_auth/profile.html")
