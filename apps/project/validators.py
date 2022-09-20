from django.core.exceptions import ValidationError


def validate_hex_value(value):
    try:
        int(value, 16)
    except ValueError:
        raise ValidationError(
            '%(value)s is not an hex number',
            params={'value': value},
        )
