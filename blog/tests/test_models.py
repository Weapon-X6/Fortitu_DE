from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import AuthorProfile, Post, Tag


class TagModelTests(TestCase):
    def test_str_method(self):
        tag = Tag.objects.create(value="manila")

        self.assertTrue(tag.__str__(), tag.value)


class PostModelTests(TestCase):
    def test_str_method(self):
        user = get_user_model().objects.create(
            email="ich@cautioners.de", password="awayfrom__me?"
        )
        post = Post.objects.create(author=user, title="Turned your back on mich")

        self.assertEqual(post.__str__(), post.title)


class AuthorProfileModelTests(TestCase):
    def test_str_method(self):
        user = get_user_model().objects.create(
            email="mesa@arizona.com", password="dont_lkTshould?"
        )
        author = AuthorProfile.objects.create(user=user)

        self.assertEqual(author.__str__(), "mesa@arizona.com")
