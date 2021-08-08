from django.urls import path, include 
from . import views
app_name = "spotify"
urlpatterns = [ 
    path("", views.index, name="index"),
    path("authorize", views.authorize, name="authorize"),
    path("callback", views.callback, name="callback"),
    path("short_term", views.short_term, name="short_term"),
    path("medium_term", views.medium_term, name="medium_term"),
    path("long_term", views.long_term, name="long_term"),
]