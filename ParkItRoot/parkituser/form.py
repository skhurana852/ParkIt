from django import forms
from .models import ParkItSpaceProvider

class SpaceProviderForm(forms.ModelForm):
    class Meta:
        model = ParkItSpaceProvider
        fields = "__all__"