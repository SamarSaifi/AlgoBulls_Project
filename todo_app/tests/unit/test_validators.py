from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from todo_app.utils.validators import validate_future_date, validate_string_length

class ValidatorTests(TestCase):
    def test_future_date_validation(self):
        # Valid future date
        future_date = timezone.now() + timedelta(days=1)
        self.assertIsNone(validate_future_date(future_date))

        # Invalid past date
        past_date = timezone.now() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            validate_future_date(past_date)

    def test_string_length_validation(self):
        # Valid string
        self.assertIsNone(validate_string_length("Test", 10, "Title"))

        # Invalid string
        with self.assertRaises(ValidationError):
            validate_string_length("Too long string", 5, "Title")