from django.urls import path
from .views import (
    ListCreateBookAPIView, 
    RetriveUpdateDestroyBookAPIView
) 

urlpatterns = [
    path('book/', ListCreateBookAPIView.as_view(), name='book-list-create'),
    path('book/<slug:slug>/', RetriveUpdateDestroyBookAPIView.as_view(), name='book-retrieve-update-delete'),
]