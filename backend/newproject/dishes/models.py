import uuid

from django.db import models


# Create your models here.
class MenuItem(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="dishes")

    def __str__(self):
        return self.name
