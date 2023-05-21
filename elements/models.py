from django.db import models


# Create your models here.
class Color(models.Model):
    color1 = models.BigIntegerField(null=True, blank=True)
    color2 = models.BigIntegerField(null=True, blank=True)

    def __int__(self):
        return self.color1


class Element(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    symbol = models.CharField(max_length=15, null=True, blank=True)
    extract = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=150, null=True, blank=True)
    atomic_weight = models.CharField(max_length=150, null=True, blank=True)
    colors = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)

    def __int__(self):
        return self.id
