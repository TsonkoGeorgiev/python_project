from django.contrib.auth.models import User
from django.db import models


class Bike(models.Model):
    MAKE_TYPES = [
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

    BODY_TYPES = [
        ('custom cruiser', 'Custom Cruiser'),
        ('super sports', 'Super Sports'),
        ('naked', 'Naked'),
        ('tourer', 'Tourer'),
        ('adventure', 'Adventure'),
    ]

    make = models.CharField(max_length=30, blank=False, choices=MAKE_TYPES)
    reg_year = models.IntegerField()
    mileage = models.IntegerField()
    engine_size = models.IntegerField()
    body_type = models.CharField(max_length=14, choices=BODY_TYPES)
    price = models.IntegerField(blank=False)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='bike_store')
    is_used = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} - {self.reg_year} - EUR {self.price}'


