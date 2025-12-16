from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Post

class TestAuth(TestCase):
    def test_register_creates_user(self):
        resp = self.client.post(reverse("register"), {
            "username": "newuser",
            "email": "new@test.com",
            "password1": "StrongPass123!@#",
            "password2": "StrongPass123!@#",
        })

        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login(self):
        User.objects.create_user("user", "u@test.com", "pass")

        resp = self.client.post(reverse("login"), {
            "username": "user",
            "password": "pass",
        })

        self.assertEqual(int(self.client.session["_auth_user_id"]),
                        User.objects.get(username="user").id)
