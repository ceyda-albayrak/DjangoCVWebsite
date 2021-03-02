from django.urls import path
from .views import CVCreateView,ViewCV,AnasayfaView,CvList,UpdateCV,DeleteCV
from .models import CV

urlpatterns=[
    path('',AnasayfaView.as_view(), name="home"),
    path('create/', CVCreateView.as_view(), name="create"),
    path('<int:pk>/', ViewCV.as_view(), name="view-cv"),
    path('<int:pk>/edit/', UpdateCV.as_view(), name="update-cv"),
    path('<int:pk>/delete/', DeleteCV.as_view(), name="delete-cv"),
    path('list/', CvList.as_view(), name="cv-list"),
    
 
   
   
]