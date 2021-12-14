from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_image = models.ImageField(blank=True, null=True)
    facebook_link = models.TextField(blank=True, null=True)
    twitter_link = models.Model(blank=True, null=True)
    google_plus_link = models.Model(blank=True, null=True)
    vine_link = models.Model(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
