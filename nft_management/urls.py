from django.urls import path
from . import views


urlpatterns = [
    path('nft-crud/<int:pk>/',views.NFTView.as_view(), name="nft"),
    path('nft-list', views.NFTListView.as_view(), name='nft-list')
]