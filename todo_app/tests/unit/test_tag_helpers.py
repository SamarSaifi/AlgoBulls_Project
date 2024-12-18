from django.test import TestCase
from todo_app.utils.tag_helpers import clean_tags

class TagHelperTests(TestCase):
    def test_clean_tags(self):
        # Test duplicate removal
        tags = ['test', 'test', 'unique']
        self.assertEqual(clean_tags(tags), ['test', 'unique'])

        # Test empty tag removal
        tags = ['test', '', '  ', 'valid']
        self.assertEqual(clean_tags(tags), ['test', 'valid'])

        # Test whitespace handling
        tags = [' test ', '  valid  ']
        self.assertEqual(clean_tags(tags), ['test', 'valid'])