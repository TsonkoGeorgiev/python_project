from django import forms

from bike_store.models import Bike
from bike_store.validators import reg_year_validator


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
        super().__init__(*args, **kwargs)

        for (_, v) in self.fields.items():
            v.widget.attrs['disabled'] = True
            v.widget.attrs['readonly'] = True


class FilterForm(forms.Form):
    MAKE_TYPES = [
        ('any', 'Any'),
        ('APRILIA', 'APRILIA'),
        ('BENELLI', 'BENELLI'),
        ('BMW', 'BMW'),
        ('DUCATI', 'DUCATI'),
        ('FIAT', 'FIAT'),
        ('HANWAY', 'HANWAY'),
        ('HARLEY-DAVIDSON', 'HARLEY-DAVIDSON'),
        ('HONDA', 'HONDA'),
        ('HYOSUNG', 'HYOSUNG'),
        ('KAWASAKI', 'KAWASAKI'),
        ('KEEWAY', 'KEEWAY'),
        ('KTM', 'KTM'),
        ('LEXMOTO', 'LEXMOTO'),
        ('MONDIAL', 'MONDIAL'),
        ('MOTO GUZZI', 'MOTO GUZZI'),
        ('PIAGGIO', 'PIAGGIO'),
        ('ROYAL ENFIELD', 'ROYAL ENFIELD'),
        ('SUZUKI', 'SUZUKI'),
        ('TRIUMPH', 'TRIUMPH'),
        ('YAMAHA', 'YAMAHA'),
    ]

    MILEAGE_CHOICES = [
        ('any', 'Any'),
        ('0-1000', 'Under 1000'),
        ('1001-5000', '1001-5000'),
        ('5001-10000', '5001-10000'),
        ('10001-999999', 'Over 10000'),
    ]

    ENGINE_CHOICES = [
        ('any', 'Any'),
        ('0-125', 'Under 125cc'),
        ('126-500', '126-500'),
        ('501-1000', '501-1000'),
        ('1001-999999', 'Over 1000'),
    ]

    BODY_TYPE_CHOICES = [
        ('any', 'Any'),
        ('custom cruiser', 'Custom Cruiser'),
        ('super sports', 'Super Sports'),
        ('naked', 'Naked'),
        ('tourer', 'Tourer'),
        ('adventure', 'Adventure'),
    ]

    PRICE_CHOICES = [
        ('any', 'Any'),
        ('0-1000', 'Under 1000'),
        ('1001-5000', '1001-5000'),
        ('5001-10000', '5001-10000'),
        ('10001-999999', 'Over 10000'),
    ]

    IS_USED_CHOICES = [
        ('any', 'Any'),
        ('new', 'New'),
        ('used', 'Used'),
    ]

    make = forms.ChoiceField(choices=MAKE_TYPES, required=False)
    reg_year = forms.IntegerField(required=False,
                                  validators=[reg_year_validator],
                                  )
    mileage = forms.ChoiceField(choices=MILEAGE_CHOICES, required=False)
    engine_size = forms.ChoiceField(choices=ENGINE_CHOICES, required=False)
    body_type = forms.ChoiceField(choices=BODY_TYPE_CHOICES, required=False)
    price = forms.ChoiceField(choices=PRICE_CHOICES, required=False)
    is_used = forms.ChoiceField(choices=IS_USED_CHOICES, required=False)




