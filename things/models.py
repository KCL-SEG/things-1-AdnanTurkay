from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=20)
    quantity = models.IntegerField()
