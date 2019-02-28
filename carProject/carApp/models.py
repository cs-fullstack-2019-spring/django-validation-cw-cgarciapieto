from django.db import models

# car Model with input/attributes make, model, year, mpg

class CarModel(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(default=0)
    mpg = models.IntegerField(default=0)

    def __str__(self):
        return self.make