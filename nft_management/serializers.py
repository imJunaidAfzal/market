
from rest_framework.serializers import ModelSerializer
from .models import Nft


class NFTSerializer(ModelSerializer):

    class Meta:
        model = Nft
        fields = '__all__'
        read_only_fields = ('owner_id','total_views',"is_hidden","is_put_on_sale","updated_at","collection_id","is_removed","nft_image")


