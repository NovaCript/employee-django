from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(
        "people.Country",
        null=True, related_name="cities",
        on_delete=models.CASCADE
    )



class Citizen(models.Model):
    full_name = models.CharField(max_length=255)
    city = models.ForeignKey(
        "people.City",
        null=True, related_name="citizens",
        on_delete=models.CASCADE
    )
