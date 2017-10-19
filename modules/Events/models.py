from django.db import models

# Create your models here.

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


class Comment(models.Model):
	id_comment = models.AutoField(primary_key=True,unique=True)
	id_event = models.ForeingKey(Event)
	comment = models.CharField(max_length=150)

'''
#Country and country_state

class Country(models.Model):
	id_country = models.AutoField(primary_key=True,unique=True)
	name_country = models.CharField(max_length=100)

#Country_state

class Country_state(models.Model):
	id_country_state = models.AutoField(primary_key=True,unique=True)
	id_country = models.ForeingKey(Country)
	state = models.CharField(max_length=100)


#Profile Photo
class Profile_photo(models.Model):
	id_profile_photo = models.AutoField(primary_key=True,unique=True)
	profile_photo = models.URLField()



#Cover Photo
class Cover_photo(models.Model):
	id_cover_photo = models.AutoField(primary_key=True,unique=True)
	cover_photo = models.URLField()
'''