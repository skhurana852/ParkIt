from .SpaceFinder.space_finder import SpaceFinder
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return render(request, "home.html")

def view_parking_space(request):
    if request.method == "POST":
        city = request.POST.get("city")
        area = request.POST.get("area")
        space_finder_ob = SpaceFinder()
        space_finder_ob.city = city
        space_finder_ob.area = area
        parking_data = space_finder_ob.get_spaces_list()
    return render(request, 'home.html',{
        'parking_data': parking_data,
    })

    # elif request.method == "GET":
    #     return HttpResponse("you are in subindex")