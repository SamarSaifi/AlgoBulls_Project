from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(date):
    """Validate that a date is in the future."""
    if date and date < timezone.now():
        raise ValidationError("Date cannot be in the past")

def validate_string_length(value, max_length, field_name):
    """Validate string length."""
    if len(value) > max_length:
        raise ValidationError(f"{field_name} must be less than {max_length} characters")