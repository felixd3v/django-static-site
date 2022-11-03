from django.urls import path
from .views import HomeView, AboutPageView
 

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomeView.as_view(), name="home"),

]