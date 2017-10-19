from django.db import models
from modules.Users.models import User
# Create your models here.

class Event(models.Model):
	#id_event = models.AutoField(primary_key=True,unique=True)
	id_user = models.ForeignKey(User)   
	date_time = models.DateTimeField(blank=True, null=False)
	lat = models.FloatField()
	lon = models.FloatField()
	street = models.CharField(max_length=50)
	number_ext = models.CharField(max_length=10)
	number_int = models.CharField(max_length=10)
	col = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	description = models.TextField()


class Comment(models.Model):
	#id_comment = models.AutoField(primary_key=True,unique=True)
	id_event = models.ForeignKey(Event)
	comment = models.CharField(max_length=150)
