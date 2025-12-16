from django.test import TestCase
from .forms import RegisterForm, PostForm


class TestRegisterForm(TestCase):
    def test_register_form_valid(self):
        form = RegisterForm({
            "username": "testuser",
            "email": "test@example.com",
            "password1": "StrongPass123!@#",
            "password2": "StrongPass123!@#",
        })
        self.assertTrue(form.is_valid(), msg=form.errors.as_text())

    def test_register_email_is_required(self):
        form = RegisterForm({
            "username": "testuser",
            "email": "",
            "password1": "StrongPass123!@#",
            "password2": "StrongPass123!@#",
        })
        self.assertFalse(form.is_valid(), msg="Email missing but form is valid")
        self.assertIn("email", form.errors)

    def test_register_email_must_be_unique(self):
        form1 = RegisterForm({
            "username": "user1",
            "email": "duplicate@example.com",
            "password1": "StrongPass123!@#",
            "password2": "StrongPass123!@#",
        })
        self.assertTrue(form1.is_valid(), msg=form1.errors.as_text())
        form1.save()

        form2 = RegisterForm({
            "username": "user2",
            "email": "duplicate@example.com",
            "password1": "StrongPass123!@#",
            "password2": "StrongPass123!@#",
        })
        self.assertFalse(form2.is_valid(), msg="Duplicate email accepted")
        self.assertIn("email", form2.errors)


class TestPostForm(TestCase):
    def test_post_form_valid(self):
        form = PostForm({
            "title": "Quadratics",
            "content": "x" * 60,
            "status": "draft",
        })
        self.assertTrue(form.is_valid(), msg=form.errors.as_text())

    def test_post_content_min_length(self):
        form = PostForm({
            "title": "Short content",
            "content": "too short",
            "status": "draft",
        })
        self.assertFalse(form.is_valid(), msg="Content < 50 chars but form is valid")
        self.assertIn("content", form.errors)
