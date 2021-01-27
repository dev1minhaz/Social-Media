from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path
from . import views


app_name="App_Posts"

urlpatterns=[
    path('',views.home,name="home"),
    path('liked/<pk>/',views.liked,name="liked"),
    path('unliked/<pk>/',views.unliked,name="unliked"),
]