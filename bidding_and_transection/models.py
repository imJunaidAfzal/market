from django.contrib.auth.models import User
from django.db import models
from NFT_Marketplace.nft_management.models import Nft
from NFT_Marketplace.wallet_management.models import Wallet


class Bidding(models.Model):
    offer_by = models.ForeignKey(User, related_name="user_biding", on_delete=models.PROTECT, null=False)
    bidding_date = models.DateTimeField(auto_now=True)
    price = models.FloatField(null=False, blank=False)
    expiry_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)  # Accepted or Rejected
    nft_id = models.ForeignKey(Nft, related_name="biding_item", on_delete=models.CASCADE, null=True)


class NftTransaction(models.Model):
    buyer_id = models.ForeignKey(User, related_name="item_buyer", on_delete=models.PROTECT, null=False)
    seller_id = models.ForeignKey(User, related_name="item_buyer", on_delete=models.PROTECT, null=False)
    nft_id = models.ForeignKey(Nft, related_name="item_transaction", on_delete=models.CASCADE, null=False)
    sold_price = models.FloatField(null=False, blank=False)
    sold_date = models.DateTimeField(auto_now=True)
    wallet_id = models.OneToOneField(Wallet, related_name="user_wallet", on_delete=models.CASCADE, null=False)
    service_fee = models.FloatField(default=0)

