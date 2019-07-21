from django.db import models

class Reservoir(models.Model):
    water_levels = models.FloatField()

    def __str__(self):
        return "Reservatório #{0}".format(self.id)
