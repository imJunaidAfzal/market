from django.contrib import admin
from . import models

admin.site.register(models.Nft)
admin.site.register(models.Category)
admin.site.register(models.Collection)
admin.site.register(models.NftPriceHistory)
admin.site.register(models.FavouriteNft)
admin.site.register(models.ReportedNft)