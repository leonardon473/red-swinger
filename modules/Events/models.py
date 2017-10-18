from django.db import models

# Create your models here.
class Event(models.Model):
	id_event = models.AutoField(primary_key=True,unique=True)
	date_time = models.DateTimeField(blank=True, null=False)
	lat = models.FloatField(max_digits=3,decimal_places=4)
	lon = models.FloatField(max_digits=3,decimal_places=4)
	address = models.CharField(max_length=250)
	description = models.TextField()
