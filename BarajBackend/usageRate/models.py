from django.db import models


class usageRate(models.Model):

    usageField = models.CharField(max_length=20)
    usageRate = models.IntegerField()
    
    




