from django.db import models

# Create your models here.
class regionalInfo(models.Model):
    region_number=models.PositiveSmallIntegerField()
    name=models.CharField(max_length=200)
    population_size=models.PositiveBigIntegerField()
    area_km=models.FloatField()
    capital_city=models.CharField(max_length=200)
    flag=models.ImageField(upload_to='flag')
    map=models.ImageField(upload_to='map')

    def __str__(self):
        return self.name