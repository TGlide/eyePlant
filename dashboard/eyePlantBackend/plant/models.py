from django.db import models
from reservoir.models import Reservoir

class Plant(models.Model):
    reservoir = models.ForeignKey(Reservoir, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    humidity = models.FloatField()
    light = models.FloatField()

    def __str__(self):
        return "Planta {0}".format(self.name)

    def to_dict(self):
        return {
            "name": self.name,
            "humidity": self.humidity,
            "light": self.light,
        }
