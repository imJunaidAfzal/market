from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.renderers import JSONRenderer, AdminRenderer

from .serializers import *


class CreateBiding(CreateAPIView):
    queryset =  Biding.objects.all()
    serializer_class = BidingSerializer
    renderer_classes = [JSONRenderer, AdminRenderer]


class GetBidingList(ListAPIView):
    queryset = Biding.objects.all()
    serializer_class = BidingSerializer
    renderer_classes = [JSONRenderer, AdminRenderer]


class SpecificBidList(RetrieveAPIView):
    queryset =  Biding.objects.all()
    serializer_class = BidingSerializer
    renderer_classes = [JSONRenderer, AdminRenderer]

    # def get_queryset(self):
    #     item_id = self.request.GET.get('item_id')
    #     queryset = Biding.objects.filter(is_removed=False,item_id=item_id)
    #     return queryset

