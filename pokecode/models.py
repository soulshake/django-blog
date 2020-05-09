from django.db import models

# Create your models here.
class Pannel(models.Model):
	name = models.CharField(max_length=300)
	image = models.ImageField(upload_to='images')
	music = models.FileField(upload_to='musics')

	def __str__(self):
		return self.name