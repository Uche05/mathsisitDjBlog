from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Post


class TestPostCRUDViews(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(
            username="author", email="author@test.com", password="pass12345"
        )
        self.other = User.objects.create_user(
            username="other", email="other@test.com", password="pass12345"
        )

        self.post = Post.objects.create(
            author=self.author,
            title="Original title",
            content="x" * 60,
            status="draft",
        )

    # create functionality test
    def test_create_requires_login(self):
        resp = self.client.get(reverse("post_create"))
        self.assertEqual(resp.status_code, 302)  # usually redirect to login

    def test_create_post_success(self):
        self.client.login(username="author", password="pass12345")

        resp = self.client.post(reverse("post_create"), {
            "title": "New post",
            "content": "y" * 60,
            "status": "draft",
        })

        self.assertEqual(Post.objects.filter(title="New post", author=self.author).count(), 1)

    def test_create_post_invalid_content_rejected(self):
        self.client.login(username="author", password="pass12345")

        resp = self.client.post(reverse("post_create"), {
            "title": "Bad post",
            "content": "too short",
            "status": "draft",
        })

        self.assertEqual(Post.objects.filter(title="Bad post").count(), 0)

    #  read functionality test
    def test_post_list_page_loads(self):
        resp = self.client.get(reverse("post_list"))
        self.assertEqual(resp.status_code, 200)

    
    # update functionality test
    def test_author_can_edit_post(self):
        self.client.login(username="author", password="pass12345")

        resp = self.client.post(reverse("post_edit", args=[self.post.slug]), {
            "title": "Updated title",
            "content": "z" * 60,
            "status": "draft",
        })

        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated title")

    # delete functionality test
    def test_author_can_delete_post(self):
        self.client.login(username="author", password="pass12345")

        resp = self.client.post(reverse("post_delete", args=[self.post.slug]))

        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_non_author_cannot_delete_post(self):
        self.client.login(username="other", password="pass12345")

        resp = self.client.post(reverse("post_delete", args=[self.post.slug]))

        self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())

# read published posts
    def test_published_post_detail_is_200(self):
        self.post.status = "published"
        self.post.save()
        resp = self.client.get(reverse("post_detail", args=[self.post.slug]))
        self.assertEqual(resp.status_code, 200)

#  read draft posts
    def test_draft_post_detail_is_404_for_anonymous(self):
        resp = self.client.get(reverse("post_detail", args=[self.post.slug]))
        self.assertEqual(resp.status_code, 404)