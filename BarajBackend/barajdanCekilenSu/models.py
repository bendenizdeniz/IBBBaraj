from django.db import models


class damVolume(models.Model):

    year = models.IntegerField()
    volume = models.IntegerField()
    area = models.CharField(max_length=15)
    


    
    




