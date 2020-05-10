from django.db import models
from PIL import Image

# Create your models here.
class Pannel(models.Model):
	name = models.CharField(max_length=300)
	image = models.ImageField(upload_to='static/pokecode/images')
	music = models.FileField(upload_to='static/pokecode/musics')

	def __str__(self):
		return self.name 

	def save_pannel(self):
		self.Image = Image.open(self.image).resize(100,100)
		self.save()

class Card(models.Model):
	true = models.ForeignKey(Pannel, on_delete=models.CASCADE, related_name='Card')
	falsees = models.ManyToManyField(Pannel)

	def __str__(self):
		return self.true.name 
