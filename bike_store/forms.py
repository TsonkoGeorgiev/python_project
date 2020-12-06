from django import forms

from bike_store.models import Bike


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'


class FilterForm(forms.Form):
    MAKE_CHOICES = [
        ('BMW', 'BMW'),
    ]

    make = forms.ChoiceField(choices=MAKE_CHOICES, required=True)
