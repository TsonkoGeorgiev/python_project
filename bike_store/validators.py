from django.core.exceptions import ValidationError


def reg_year_validator(value):
    if value <= 0:
        raise ValidationError('Must be a positive value')
