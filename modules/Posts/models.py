from django.db import models

# Create your models here.

class Posts(models.Model):
	id_post = models.AutoField(primary_key=True,unique=True)
	id_user = models.ForeingKey()
	text = models.TextField()
	image = models.URLField()

class Comment(models.Model)
	id_comment = models.AutoField(primary_key=True,unique=True)
	id_post = models.ForeingKey(Posts)
	comment = models.CharField(max_length=150)



