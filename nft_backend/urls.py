from django.urls import path

from . import views

urlpatterns = [
    path('create-bid/', views.CreateBiding.as_view(), name='create-bid'),
    path('get-bid-list/', views.GetBidingList.as_view(), name='update-bid'),
    path('specific-bid-list/<int:pk>/', views.SpecificBidList.as_view(), name='specific-bid')
]
