from django import forms

from bike_store.models import Bike


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        exclude = ('user',)

    def clean_reg_year(self):
        reg_year = self.cleaned_data['reg_year']
        if reg_year < 0:
            raise forms.ValidationError('Cannot provide negative values')
        return reg_year

    def clean_mileage(self):
        mileage = self.cleaned_data['mileage']
        if mileage < 0:
            raise forms.ValidationError('Cannot use negative values')
        return mileage

    def clean_engine_size(self):
        engine_size = self.cleaned_data['engine_size']
        if engine_size < 0:
            raise forms.ValidationError('Cannot use negative values')
        return engine_size

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Cannot use negative values')
        return price


class DeleteBikeForm(BikeForm):
    def __init__(self, *args, **kwargs):
        BikeForm.__init__(self, *args, **kwargs)

        for (_, v) in self.fields.items():
            v.widget.attrs['disabled'] = True
            v.widget.attrs['readonly'] = True

