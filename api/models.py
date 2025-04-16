from django.db import models

# Create your models here.
class Logger(models.Model):
    pdf_url = models.CharField(max_length=500)
    accessibility_report = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    #ip = models.FloatField()
    #time = models.TimeField()
    #process_time = models.FloatField()
    #size = models.FloatField()
    #pages = models.IntegerField()

    def __str__(self):

        return self.name