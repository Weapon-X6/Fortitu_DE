from django.test import TestCase

from blango_auth.models import User
from blog.templatetags import blog_extras


class CustomTemplateTagstests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User(email="noheart@nopain.de", password="forgetit")
        cls.current_user = User(email="kein@risque.de", password="déçu*23")

    def test_author_details_when_author_is_empty(self):
        res = blog_extras.author_details([], None)

        self.assertEqual("", res)

    def test_author_details_when_author_is_current_user(self):
        current_user = self.author

        res = blog_extras.author_details(self.author, current_user)

        self.assertEqual("<strong>me</strong>", res)

    def test_author_details_when_author_has_not_any_name(self):
        res = blog_extras.author_details(self.author, self.current_user)

        self.assertEqual(
            f'<a href="mailto:{self.author.email}"> {self.author.email} </a>', res
        )

    def test_author_details_when_author_has_both_names(self):
        self.author.first_name = "_"
        self.author.last_name = "head"

        res = blog_extras.author_details(self.author, self.current_user)

        self.assertEqual(
            f'<a href="mailto:{self.author.email}"> {self.author.first_name} {self.author.last_name} </a>',
            res,
        )
