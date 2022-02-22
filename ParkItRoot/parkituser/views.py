from .SpaceFinder.space_finder import SpaceFinder
from django.http import HttpResponse
from django.shortcuts import render
import json
from parkituser.models import ParkItSpaceProvider

def view_parking_space(request):
    if request.method == "POST":
        city = request.POST.get("city")
        area = request.POST.get("area")
        spaces = list(ParkItSpaceProvider.objects.filter(city=city, area=area).values())
        return render(request, 'home.html',{
            'parking_data': spaces,
        })

    elif request.method == "GET":
        return render(request, "home.html")