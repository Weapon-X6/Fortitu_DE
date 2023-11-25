from django.test import TestCase

from blog.forms import CommentForm


class CommentFormTests(TestCase):
    def test_invalid_form(self):
        form = CommentForm(data={"content": ""})

        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        form = CommentForm(data={"content": "I'm not scared!"})

        self.assertTrue(form.is_valid())
