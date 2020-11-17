from django.db import models

# Create your models here.

class Car(models.Model):
    vendor = models.CharField(max_length=280)
    model = models.CharField(max_length=280)
    year = models.PositiveSmallIntegerField()
    volume = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [
            ('vendor','model','year'),
        ]

