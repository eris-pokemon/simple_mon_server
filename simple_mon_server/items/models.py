from django.db import models


class Item(models.Model):
    """
    Store the attributes of an item.
    Presently only has the name and a description of the item.
    """
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
