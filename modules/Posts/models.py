from django.db import models

# Create your models here.

class Posts(models.Model):
	id_post = models.PrimaryKey(primary_key=True,unique=True)
	id_user = models.ForeingKey()
	text = models.TextField()
	image = models.URLField()
