from django.db import models


class VesselCategory(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Vessel(models.Model):
    category = models.ForeignKey(VesselCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
