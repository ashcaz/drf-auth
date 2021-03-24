from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Tool


class ToolTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_tool = Tool.objects.create(
            name="JigSaw",
            owner=testuser1,
            price=39.99,
            description="Get them while they are hot",
            number_in_inventory=5,
        )
        test_tool.save()

    def test_tool_content(self):
        tool = Tool.objects.get(id=1)
        actual_name = str(tool.name)
        actual_owner = str(tool.user)
        actual_price = float(tool.price)
        actual_description = str(tool.description)
        actual_inventory = int(tool.number_in_inventory)
        self.assertEqual(actual_name, "JigSaw")
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_price, 39.99)
        self.assertEqual(actual_description, "Get them while they are hot")
        self.assertEqual(actual_inventory, 5)