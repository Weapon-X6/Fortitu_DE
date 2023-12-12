from datetime import datetime
from http import HTTPStatus

import pytz
from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Post


class BlogTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            email="wheredowegofrom@here.sv", password="wnf_alone"
        )
        cls.user2 = get_user_model().objects.create(
            email="wheredowegofrom@wnf.sv", password="wnf_beba*23"
        )

        cls.published_post = Post.objects.create(
            author=cls.user,
            title="Danger",
            content="Just give me some ease to me...",
            slug="gave-everything",
            published_at=datetime(2023, 11, 19, 19, 58, 35, tzinfo=pytz.UTC),
        )
        cls.unpublished_post = Post.objects.create(
            author=cls.user,
            title="It Feels Like",
            content="The only way is the wrong way...",
            slug="it-feels-like",
        )

    def test_index(self):
        response = self.client.get("")

        self.assertTrue(response.status_code, HTTPStatus.OK)
        self.assertNotContains(response, self.unpublished_post.title)
        self.assertContains(response, self.published_post.title)
        self.assertContains(response, self.published_post.summary)
        self.assertTemplateUsed(response, "blog/index.html")

    def test_get_detail_anonymously(self):
        response = self.client.get(f"/post/{self.published_post.slug}/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_post.content)
        self.assertTemplateUsed(response, "blog/post-detail.html")
        self.assertTemplateUsed(response, "blog/post-byline.html")
        self.assertTemplateUsed(response, "blog/post-comments.html")
        self.assertTemplateUsed(response, "blog/post-recent-list.html")
        self.assertNotContains(response, "<h5>Add Comment</h5>", html=True)

    def test_get_detail_authenticated(self):
        self.client.force_login(self.user2)
        response = self.client.get(f"/post/{self.published_post.slug}/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h5>Add Comment</h5>", html=True)

    def test_get_detail_authenticated_my_post(self):
        self.client.force_login(self.user)

        response = self.client.get(f"/post/{self.published_post.slug}/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotContains(response, "<h5>Add Comment</h5>", html=True)

    def test_post_detail(self):
        self.client.force_login(self.user2)
        payload = {"content": "The Art of Dying"}

        response = self.client.post(f"/post/{self.published_post.slug}/", payload)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_post_table(self):
        response = self.client.get("/post-table/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "blog/post-table.html")
