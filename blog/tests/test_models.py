from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import AuthorProfile, Post, Tag


class TagModelTests(TestCase):
    def test_str_method(self):
        tag = Tag.objects.create(value="manila")

        self.assertTrue(tag.__str__(), tag.value)


class PostModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create(
            email="ich@cautioners.de", password="awayfrom__me?"
        )
        cls.post = Post.objects.create(
            author=user, title="Turned your back on mich", slug="Pacita"
        )

    def test_str_method(self):
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_get_absolute_url(self):
        canonical_url = self.post.get_absolute_url()

        self.assertEqual(canonical_url, f"/post/{self.post.slug}/")


class AuthorProfileModelTests(TestCase):
    def test_str_method(self):
        user = get_user_model().objects.create(
            email="mesa@arizona.com", password="dont_lkTshould?"
        )
        author = AuthorProfile.objects.create(user=user)

        self.assertEqual(author.__str__(), "mesa@arizona.com")
