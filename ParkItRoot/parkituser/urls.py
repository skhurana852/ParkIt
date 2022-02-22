from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_parking_space, name="view_parking_space" )
]