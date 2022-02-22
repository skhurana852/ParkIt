from django.contrib import admin
from parkituser.models import ParkItSpaceProvider
# Register your models here.

class ParkItAdmin(admin.ModelAdmin):
    pass

admin.site.register(ParkItSpaceProvider, ParkItAdmin)
