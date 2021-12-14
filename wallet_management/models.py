from django.contrib.auth.models import User
from django.db import models


class Wallet(models.Model):
    user_id = models.ForeignKey(User, related_name="user_wallet", on_delete=models.CASCADE, null=False)
    current_balance = models.FloatField(default=0)
    wallet_address = models.TextField(null=False, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)


class WalletTransaction(models.Model):
    wallet_id = models.OneToOneField(Wallet, related_name="wallet_transaction", on_delete=models.CASCADE, null=False)
    amount = models.FloatField(null=False, blank=False)

    choices = [
        ("pay", "Pay"),
        ("deposit", "Deposit"),
        ("received", "Received")
    ]
    transaction_type = models.TextField(max_length=40, choices=choices, blank=False, null=False)
    transaction_date = models.DateTimeField(auto_now=True)
