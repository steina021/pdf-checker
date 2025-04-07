from django.db import models

# Create your models here.
class Logger(models.Model):

    test = models.CharField(max_length=100)

    #ip = models.FloatField()
    #time = models.TimeField()
    #process_time = models.FloatField()
    #size = models.FloatField()
    #pages = models.IntegerField()

    def __str__(self):

        return self.name