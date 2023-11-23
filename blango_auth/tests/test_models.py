from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(email="", password="l_hiver2020")

        user = get_user_model().objects.create_user(
            email="enfat@sauvage.fr", password="l_hiver2020"
        )

        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email="enfat@sauvage.fr", password="l_hiver2020"
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(
                email="pain@master.is", password="l_hiver2020", is_staff=False
            )
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(
                email="haunting@me.de", password="l_hiver2020", is_superuser=False
            )
