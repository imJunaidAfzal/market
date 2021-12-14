from user_management.models import User
from django.db import models
from nft_management.models import Category


class Contact(models.Model):
    name = models.TextField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.TextField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    contact_date = models.DateTimeField(auto_now=True)
    is_responded = models.BooleanField(default=False)
    resolved_by = models.ForeignKey(User, related_name="resolved_user", on_delete=models.PROTECT, null=True)
    resolved_date = models.DateTimeField(blank=True, null=True)
    is_removed = models.BooleanField(default=False)


class FAQ(models.Model):
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    updated_by = models.ForeignKey(User, related_name="FAQ_user", on_delete=models.PROTECT, null=True)
