from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post

class TestPostModel(TestCase):
    def test_slug_is_generated_on_save(self):
        user = User.objects.create_user("user", "u@test.com", "pass")
        post = Post.objects.create(
            author=user,
            title="My Test Post",
            content="x" * 60,
            status="draft",
        )
        self.assertEqual(post.slug, "my-test-post")

    def test_slug_is_unique(self):
        user = User.objects.create_user("user", "u@test.com", "pass")

        post1 = Post.objects.create(
            author=user,
            title="Same Title",
            content="x" * 60,
        )
        post2 = Post.objects.create(
            author=user,
            title="Same Title",
            content="x" * 60,
        )

        self.assertNotEqual(post1.slug, post2.slug)
