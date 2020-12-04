from django.db import models


class Bike(models.Model):
    BODY_TYPES = [
        ('custom cruiser', 'Custom Cruiser'),
        ('super sports', 'Super Sports'),
        ('naked', 'Naked'),
        ('tourer', 'Tourer'),
        ('adventure', 'Adventure'),
    ]

    name = models.CharField(max_length=30, blank=False)
    reg_year = models.IntegerField()
    mileage = models.IntegerField()
    engine_size = models.IntegerField()
    body_type = models.CharField(max_length=14, choices=BODY_TYPES)
    price = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='bike_store')
    is_used = models.BooleanField()

    def __str__(self):
        return f'{self.name} - {self.reg_year} - {self.price}'
