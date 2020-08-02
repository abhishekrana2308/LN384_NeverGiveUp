from django.db import models


# Create your models here.
class Sector(models.Model):
    name = models.CharField(max_length=100)
    fields = models.TextField()

    def __str__(self):
        return self.name

class Electricity(models.Model):
	Actual_flow_min = models.IntegerField(default=0)
	Actual_flow_max = models.IntegerField(default=0)
	Frequency_min = models.IntegerField(default=0)
	Frequency_max = models.IntegerField(default=0)
	Date_updated = models.TextField()

