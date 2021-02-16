from django.urls import path
from .views import AnasayfaView

urlpatterns = [
    path('',AnasayfaView.as_view(), name="haberler")
]