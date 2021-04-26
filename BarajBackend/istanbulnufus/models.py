from django.db import models


class istanbulNufus(models.Model):

    year = models.IntegerField(unique=True)
    population = models.FloatField()
   

    


   

