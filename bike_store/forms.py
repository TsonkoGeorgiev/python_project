from django import forms

from bike_store.models import Bike


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'
