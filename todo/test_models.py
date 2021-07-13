from django.test import TestCase
from .models import Item


class testDone(TestCase):
    def test_done_status(self):
        item = Item.objects.create(name="get item")
        self.assertFalse(item.done)
        
    def test_item_of_string_item(self):
        item = Item.objects.create(name="get item")
        self.assertEqual(str(item), "get item")