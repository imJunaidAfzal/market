from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.TextField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_removed = models.BooleanField(default=False)


class Collection(models.Model):
    collection_name = models.CharField(max_length=200, null=False, blank=False)
    logo_image = models.ImageField(blank=True, null=True)
    banner_image = models.ImageField(blank=True, null=True)
    collection_description = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    category_id = models.ForeignKey(Category, related_name="item_category", on_delete=models.PROTECT, null=True)
    user_id = models.ForeignKey(User, related_name="profile_user", on_delete=models.CASCADE, null=False)
    is_removed = models.BooleanField(default=False)


class Nft(models.Model):
    nft_name = models.CharField(blank=False, null=False)
    nft_description = models.CharField(blank=True, null=True)
    nft_image = models.ImageField(null=False, blank=False)
    royalty = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    choices = [
        ("is_put_on_sale", "Is Put On Sale"),
        ("is_instant_sale_price", "Is Instant Sale Price"),
        ("is_unlock_purchase", "Is Unlock Purchase")
    ]
    sale_type = models.CharField(max_length=40, choices=choices, null=True, blank=True)
    is_hidden = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    collection_id = models.ForeignKey(Collection, related_name="item_collection", on_delete=models.CASCADE, null=False)
    owner_id = models.ForeignKey(User, related_name="item_user", on_delete=models.CASCADE, null=False)
    total_views = models.IntegerField(default=0)


class NftPriceHistory(models.Model):
    nft_id = models.ForeignKey(Nft, related_name="item_history", on_delete=models.CASCADE, null=False)
    price = models.FloatField(null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)


class FavouriteNft(models.Model):
    user_id = models.ForeignKey(User, related_name="user_favourite", on_delete=models.CASCADE, null=False)
    nft_id = models.ForeignKey(Nft, related_name="favourite_item", on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now=True)
    is_removed = models.BooleanField(default=False)


class ReportedNft(models.Model):
    nft_id = models.ForeignKey(Nft, related_name="favourite_item", on_delete=models.CASCADE, null=False)
    reporter_id = models.ForeignKey(User, related_name="user_favourite", on_delete=models.CASCADE, null=False)
    choices = [
        ("fake", "Fak or spam"),
        ("explicit", "Explicit and Sensitive Content"),
        ("might_be_stolen", "Might be Stolen"),
        ('other', 'Other')
    ]
    report_type = models.CharField(max_length=40, choices=choices, null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
