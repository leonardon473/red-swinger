from django.db import models

# Create your models here.

class Comment(models.Model)
	id_comment = models.AutoField(primary_key=True,unique=True)
	comment = models.CharField(max_length=150)


class Posts(models.Model):
	id_post = models.AutoField(primary_key=True,unique=True)
	id_comment = models.ForeingKey(Comment)
	text = models.TextField()
	image = models.URLField()





