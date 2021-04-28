from django.db import models


class istanbulNufus(models.Model):

    year  = models.IntegerField()
    population = models.IntegerField()
    givenWater = models.IntegerField(default=-1)
   

    


   

