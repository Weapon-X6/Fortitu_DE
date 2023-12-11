from datetime import datetime
from http import HTTPStatus

import pytz
from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Post


class BlogTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create(
            email="wheredowegofrom@here.sv", password="wnf_alone"
        )

        cls.published_post = Post.objects.create(
            author=user,
            title="Danger",
            content="Just give me some ease to me...",
            slug="gave-everything",
            published_at=datetime(2023, 11, 19, 19, 58, 35, tzinfo=pytz.UTC),
        )
        cls.unpublished_post = Post.objects.create(
            author=user,
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

    def test_post_detail_get(self):
        response = self.client.get(f"/post/{self.published_post.slug}/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_post.content)
        self.assertTemplateUsed(response, "blog/post-detail.html")
        self.assertTemplateUsed(response, "blog/post-byline.html")
        self.assertTemplateUsed(response, "blog/post-comments.html")
        self.assertTemplateUsed(response, "blog/post-recent-list.html")

    def test_post_detail_post(self):
        user = get_user_model().objects.create(
            email="wheredowegofrom@wnf.sv", password="wnf_beba*23"
        )
        payload = {"content": "The Art of Dying", "creator": user.id}

        response = self.client.post(f"/post/{self.published_post.slug}/", payload)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_table(self):
        response = self.client.get("/post-table/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "blog/post-table.html")
