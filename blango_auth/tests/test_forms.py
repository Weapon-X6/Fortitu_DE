from django.test import TestCase

from blango_auth.forms import BlangoRegistrationForm


class RegistrationFormTests(TestCase):
    def test_unmatching_passwords(self):
        form = BlangoRegistrationForm(
            data={"email": "anda@laosa.com", "password1": "1233", "password2": "123"}
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], ["The two password fields didn’t match."]
        )

    def test_invalid_matching_passwords(self):
        form = BlangoRegistrationForm(
            data={"email": "anda@laosa.com", "password1": "123", "password2": "123"}
        )

        self.assertEqual(
            form.errors["password2"],
            [
                "This password is too short. It must contain at least 8 characters.",
                "This password is too common.",
                "This password is entirely numeric.",
            ],
        )

    def test_valid_password(self):
        form = BlangoRegistrationForm(
            data={
                "email": "anda@laosa.com",
                "password1": "Pacita*23",
                "password2": "Pacita*23",
            }
        )

        self.assertTrue(form.is_valid())
        with self.assertRaises(KeyError):
            form.errors["password2"]
