from rest_framework.serializers import ModelSerializer
from .models import Tool


class ToolSerializer(ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "owner",
            "price",
            "description",
            "number_in_inventory",
            "last_updated",
        )
        model = Tool