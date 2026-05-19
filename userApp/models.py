from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    joined = models.DateTimeField(auto_now_add=True)
    favourite_quote = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.author