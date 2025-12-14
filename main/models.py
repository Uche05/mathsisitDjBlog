from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    """
    Extends Django's User model without modifying it.
    No duplicate fields that already exist on User.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user.username}'s profile"


class Post(models.Model):
    """
    Stores a single mathematics main post.
    Linked to Django's built-in User model as the author.
    """

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def _generate_unique_slug(self):
        """
        Create a unique slug based on the title.
        If the slug already exists, append -2, -3, etc.
        """
        base_slug = slugify(self.title)[:210] or "post"
        slug = base_slug
        counter = 2

        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Stores a single comment on a Post.
    Linked to both Post and User.
    """

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
