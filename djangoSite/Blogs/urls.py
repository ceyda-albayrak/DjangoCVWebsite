from django.urls import path 
from .views import BlogListView,AnasayfaView,CreateCvView
#from .views import BlogListView

urlpatterns = [
    path('create',CreateCvView.as_view(),name="create"),
    path('blog/',BlogListView.as_view(),name="blog"),
    path('',AnasayfaView.as_view(), name="home")
]