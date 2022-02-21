from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('parkingspace',views.view_parking_space, name="view_parking_space" )
]