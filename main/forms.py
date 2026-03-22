from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Category, Post


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class LoginForm(AuthenticationForm):
    # AuthenticationForm already validates incorrect password/username.
    # We just style widgets.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"placeholder": field.label})


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "difficulty", "content", "status")

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Introduction to Quadratics"}),
            "content": forms.Textarea(attrs={"placeholder": "Write your maths explanation here..."}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "difficulty": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make category optional in the form
        self.fields["category"].required = False
        self.fields["category"].empty_label = "Select a category (optional)"

    def clean_content(self):
        content = (self.cleaned_data.get("content") or "").strip()
        if len(content) < 50:
            raise forms.ValidationError("Content must be at least 50 characters.")
        return content
