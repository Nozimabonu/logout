from django.core.exceptions import ValidationError


def validate_length(value, length=13):
    if len(str(value)) != length:
        raise ValidationError(f'{value} is not a valid length 13 characters long')


