from django.db import models

# Create your models here.

class MyBlog(models.Model):
	title = models.CharField(max_length= 50)
	description = models.TextField(max_length=500000)
	date = models.DateTimeField(auto_now= False, auto_now_add= False)

	def __str__(self):
		return self.title
