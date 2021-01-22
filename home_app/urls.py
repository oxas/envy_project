from django.urls import path, re_path
from home_app import views

urlpatterns = [
    re_path(r'^$', views.homeApp),
]
