from django.db import models
from django.contrib.auth import get_user_model


class Tool(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    number_in_inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name