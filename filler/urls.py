from django.urls import path
from . import views

app_name = "filler"
urlpatterns = [   
    path("", views.poopy, name="poopy")
]