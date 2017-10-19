from django.db import models
from modules.Users.models import User
# Create your models here.

class Comment(models.Model):
	id_user = models.ForeignKey(User)   
	id_comment = models.AutoField(primary_key=True,unique=True)
	comment = models.CharField(max_length=150)


class Posts(models.Model):
	#id_post = models.AutoField(primary_key=True,unique=True)
	id_comment = models.ForeignKey(Comment)
	text = models.TextField()
	image = models.URLField()





