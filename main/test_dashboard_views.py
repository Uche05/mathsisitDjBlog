from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Post

class TestDashboard(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("user", "u@test.com", "pass")
        self.other = User.objects.create_user("other", "o@test.com", "pass")

        Post.objects.create(
            author=self.user,
            title="My Post",
            content="x" * 60,
        )
        Post.objects.create(
            author=self.other,
            title="Other Post",
            content="x" * 60,
        )

    def test_dashboard_requires_login(self):
        resp = self.client.get(reverse("dashboard"))
        self.assertEqual(resp.status_code, 302)

    def test_dashboard_shows_only_user_posts(self):
        self.client.login(username="user", password="pass")
        resp = self.client.get(reverse("dashboard"))

        self.assertContains(resp, "My Post")
        self.assertNotContains(resp, "Other Post")
