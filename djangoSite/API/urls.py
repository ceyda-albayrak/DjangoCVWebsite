from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from API import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('token/', views.MyObtainTokenPairView.as_view()),
    path('cv-list/', views.cv_list),
    path('cv-detail/<int:pk>', views.cv_detail),
]