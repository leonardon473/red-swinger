from django.db import models

# Create your models here.

class Comment(models.Model)
	id_comment = models.AutoField(primary_key=True,unique=True)
	id_post = models.ForeingKey(Event)
	comment = models.CharField(max_length=150)


class Event(models.Model):
	id_event = models.AutoField(primary_key=True,unique=True)
	date_time = models.DateTimeField(blank=True, null=False)
	lat = models.FloatField(max_digits=3,decimal_places=4)
	lon = models.FloatField(max_digits=3,decimal_places=4)
	street = models.CharField(max_length=50)
	number_ext = models.CharField(max_length=10)
	number_int = models.CharField(max_length=10)
	col = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	description = models.TextField()

